# -*- coding: utf-8 -*-
import sys
import os.path
import re
import codecs
from StringIO import *


class TemplateProcessorNotCompleteException(Exception):
    """ Exception if not all attributes are set"""
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "TemplateProcessor is missing some information: %s not given" % args[0]
        else:
            self.message = \
                "TemplateProcessor is missing some information"


class TemplateProcessorWrongDataException(Exception):
    """ Exception if attributes are not filled with the right data types """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "You tried to put some illegal data into an TemplateProcessor attribute: %s" % args[0]
        else:
            self.message = \
                "You tried to put some illegal data into an TemplateProcessor attribute"


class TemplateProcessorUnknownAttributeException(Exception):
    """ Exception if attributes are not filled with the right data types """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "You attempted to set an unknown attribute in TemplateProcessor: Attribute %s does not exist" % args[0]
        else:
            self.message = \
                "You attempted to set an unknown attribute in TemplateProcessor"


class TemplateProcessorIllegalLoopMarkerException(Exception):
    """ Exception if you end a loop that isn't open, or access a loopvar outside of a loop """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "There are errors in the loop structure of the template file; %s occured outside of a loop" % args[0]
        else:
            self.message = \
                "There are errors in the loop structure of the template file"


class TemplateProcessorLoopDataOutOfBounds(Exception):
    """ Exception if loop data is requested with a nonexisting index """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "The index for the loop data is out of bounds (index %s)" % args[0]
        else:
            self.message = \
                "The index for the loop data is out of bounds"


class TemplateProcessorUnknownLoopVar(Exception):
    """ Exception if loop data is requested that doesn't exist """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "The loop variable %s does not exist" % args[0]
        else:
            self.message = \
                "The requested loop variable does not exist"


class TemplateProcessorErrorInLoopVarConstruction(Exception):
    """ Exception if loop data is requested that doesn't exist """
    def _init__(self, *args):
        if len(args) > 0:
            self.message = \
                "The LoopVar Object was created with illegal data:\n%s" % args[0]
        else:
            self.message = \
                "The LoopVar Object was created with illegal data"

class AttributeHolder(object):
    """
    A simple object that can hold arbitrary attributes

    Just assign and read attributes from this object, no other methods
    """
    def __setattr__(self, name, value):
        self.__dict__[name] = value

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


class LoopData(object):
    """A class for LoopData.

    It holds the length of the loop and provides the loop data.
    The object must be fully initialized on creation.
    """
    def __init__(self, length, datafunction):
        """
        Initialization takes two mandatory parameters:
        length: and integer > 0 that describes how many iterations are in the loop
        datafunction: a callable that provides the loop data

        The datafunction must have the following specifications:
        - it takes exactly two parameters: index, and varname
        - it returns a string that is the contents of varname for the iteration index
        - if the varname does not exist, it doesn't return anything (None)

        There is a public attribute 'iteration' that serves as a marker of where the
        loop is in an iteration. You have to set the attribute externally
        """
        if isinstance(length, int) and (length >= 0):
            self.length = length
        else:
            raise TemplateProcessorErrorInLoopVarConstruction("length must be an integer >= 0")
        if callable(datafunction):
            # run a test of the datafunction
            try:
                datafunction(length-1, "")
            except TypeError: # test failed
                raise TemplateProcessorErrorInLoopVarConstruction(\
                    "The data function did not pass the test call. " + \
                    "Try help(LoopData) for the specifications of a valid data function");
            else: # test succeeded
                self.datafunction = datafunction
        else:
            raise TemplateProcessorErrorInLoopVarConstruction(\
                "The data function is not callable")
        self.iteration = 0
    def __len__(self):
        return self.length
    def get(self, index, varname):
        """ Get loop data by index and varname"""
        if (index < 0) or (index >= self.length):
            raise TemplateProcessorLoopDataOutOfBounds(index)
        return self.datafunction(index, varname)



class LoopLineBlock(object):
    """ Describes a block of lines that form a loop """
    def __init__(self):
        self.i = 0
        self.lines = []
    def append(self, strline, *more_strlines):
        """ Append a string to the block, as a line """
        self.lines.append(strline)
        for line in more_strlines:
            self.lines.append(line)
    def readline(self):
        """ Return the next line in the block """
        try:
            self.i += 1
            return self.lines[self.i-1]
        except IndexError:
            return None
    def reopen(self):
        """ Reset the readline index to 0"""
        self.i = 0






class TemplateProcessor(object):
    """A html template processor.

    It reads a template file and processes it, reacting to markers in that file.

    The class has these attributes:
        template            the template file
        memorytemplate      a string to be used as template
                            Either 'template' or 'memorytemplate' has to be given.
                            If both are given, 'template' takes preference
        output              the output file, stdout if not given
        replacements        a dictionary of varnames that is used to fill the template
        loops               a dictionary of loop names mapped to LoopData objects
        indent              a string that is prepended to every line of output

    The public class variables are :
        overwrite [False]      determines if the output overwrites an existing file
        encoding ['utf-8']     the encoding of the template file and the output
        searchencodings        encodings that are tried to decode the search string
                               Default is the list ['utf-8', 'iso8859']

    These are the markers recognized in a template file:
    <!-- var <varname> -->                 is replaced by replacements[varname]
    <!-- startloop <loopname> -->          full line is deleted and starts a loop
    <!-- loopvar <loopname>.<varname> -->  replaced by loop.get(i, varname)
    <!-- endloop <loopname> -->            ends a loop
    <!-- if <expr> -->                     print block only if expression is true
    <!-- endif -->                         ends an if0-block

    All names must be from the characters [A-Za-z0-9_]

    Replacements may be in unicode.

    The markers can also have the form [!-- ... --]

    An expression in an if-marker can be any Python-expression that evaluates to
    True or False. You can uses any <varname> or <loopname<.<varname> that is valid
    in that context. For example, these can be valid expressions
        number >= str(1 + int(i))         # 'number' and 'i' are varnames
        l.string1 == l.string2            # 'loop.string1' and 'loop.string2'
                                          #    are loop-varnames in a loop 'l'
        l.string != "\"bla\""             #  quotes must be escaped
        (int(l.i) < 2) or (int(l.i) > 5)  #  something a bit more complicated


    All block markers (startloop/endloop, if/endif must be on a separate line (the
    full line is removed from the output)!
    """

    overwrite       = False
    encoding        = 'utf-8'
    searchencodings = ['utf-8', 'iso8859']
    _rx_comment     = re.compile(r'<!--.*?-->')
    _rx_comment2    = re.compile(r'\[!--.*?--\]')
    _rx_var         = re.compile(r'.!--\s*var\s+([A-Za-z0-9_]+)\s*--.')
    _rx_startloop   = re.compile(r'.!--\s*startloop\s+([A-Za-z0-9_]+)\s*--.')
    _rx_loopvar     = re.compile(r'.!--\s*loopvar\s+([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\s*--.')
    _rx_endloop     = re.compile(r'.!--\s*endloop\s+([A-Za-z0-9_]+)\s*--.')
    _rx_if          = re.compile(r'.!--\s*if\s+(.*)--.')
    _rx_else        = re.compile(r'.!--\s*else\s*--.')
    _rx_endif       = re.compile(r'.!--\s*endif\s*--.')

    def __init__(self, **args):
        """ Create a TemplateProcessor object

            Any of the class attributes can be given as optional named parameters
        """
        if args.has_key("template"):
            self.template = args["template"]
        else:
            self.__dict__["template"] = ""
        if args.has_key("output"):
            self.output = args["output"]
        else:
            self.__dict__["output"] = ""
        if args.has_key("replacements"):
            self._varreplacements = args["replacements"]
        else:
            self.__dict__["_varreplacements"] = {}
        if args.has_key("indent"):
            self.indent = args["indent"]
        else:
            self.indent = ""
        if args.has_key("loops"):
            self.loops = args["loops"]
        else:
            self.__dict__["loops"] = {}
        if args.has_key("memorytemplate"):
            self.memorytemplate = args["memorytemplate"]
        else:
            self.memorytemplate = None

        # private attributes
        self.__dict__["_outfile"]      = None # the file object for output
        self.__dict__["_templatefile"] = None # the file object for the template file
        self._replacements             = {} # full string replacements, not just varnames
        self._iteration                = {} # keeps track of how many iterations were done in a specific loop
        self._activeoutput             = True; # if this is False, all output is surpressed (used for if-blocks)
        self._if_stack                 = [] # stack for nested if's


    def __setattr__(self, name, value):
        if name == "template":
            if os.path.isfile(value):
                self.__dict__[name] = value
            else:
                raise TemplateProcessorWrongDataException("Template file does not exist");
        elif name == "memorytemplate":
            self.__dict__[name] = value
        elif name == "indent":
            self.__dict__[name] = value
        elif name == "output":
            if os.path.isfile(value):
                if self.overwrite:
                    self.__dict__[name] = value
                else:
                    raise TemplateProcessorWrongDataException(\
                        "Output file already exists, and overwrite is not set");
            else:
                self.__dict__[name] = value
        elif (name == "replacements"):
            if isinstance(value, dict):
                for k,v in value.items():
                    if not isinstance(k, basestring):
                        raise TemplateProcessorWrongDataException(\
                                "Replacements attribute must be a dictionary of strings. Some key was not a string.");
                    if not isinstance(v, basestring):
                        warn("The replacement for '%s' isn't a string... trying to fix that..." % k)
                        try:
                            value[k] = str(v)
                        except Exception:
                            warn("Can't convert the replacement for '%s' into a string" % k)
                            warn("Dropping the replacement entirely")
                            del(value[k])
                        else:
                            warn("    Fixed: replacement for '%s' was converted into the string '%s'" % (k,v))
                self.__dict__['_varreplacements'] = value
            else:
                raise TemplateProcessorWrongDataException(\
                    "Replacements attribute must be a dictionary");
        elif name == "loops":
            loopdict = value
            if isinstance(loopdict, dict):
                for loopname,loopdata in loopdict.items():
                    if not isinstance(loopname, basestring):
                        raise TemplateProcessorWrongDataException(\
                            "Loop names must be strings");
                    if not isinstance(loopdata, LoopData):
                        raise TemplateProcessorWrongDataException(\
                            "the loop %s does not point to a LoopData object" % loopname);
                self.__dict__[name] = value
            else:
                raise TemplateProcessorWrongDataException(\
                    "Loops attribute must be a dictionary");
        elif name.startswith('_'): # setting private attributes
            self.__dict__[name] = value
        else:
            raise TemplateProcessorUnknownAttributeException(name)


    def __getattr__(self, name):
        if (name == "replacements"):
            return self._varreplacements
        else:
            raise TemplateProcessorUnknownAttributeException(name)


    def run(self, to_memory=False):
        """ Processes the template and write to the output, return None

            If to_memory is set to True, don't write to the output but
            return a StringIO object instead.
        """
        if self.template == "" and self.memorytemplate == "":
            raise TemplateProcessorNotCompleteException("Template was not set")
        if not to_memory:
            self._outfile = sys.stdout
            if self.output != "":
                try:
                    self._outfile = codecs.open(self.output, "w", self.encoding)
                except IOError, args:
                    warn("%s while writing to %s" % (args.strerror, args.filename) )
                    warn("Output will be written to stdout")
        else:
            self._outfile = StringIO()
        if self.template != "":
            self._templatefile = codecs.open(self.template, "r", self.encoding)
        else:
            self._templatefile = StringIO(self.memorytemplate)
        self._handleblock()
        if to_memory:
            return self._outfile.getvalue()
        if not self._outfile is sys.stdout:
            self._outfile.close()
        self._templatefile.close()
        return None


    def _handleblock(self, **blockdata):
        """
        Handle a block in the template

        This can be the entire template, or a loop block
        """
        isloopblock = blockdata.has_key('block') # distinguishes if we're dealing with the full template, or a loop block
        block = self._templatefile
        loopname = None

        if isloopblock:
            try:
                block = blockdata['block']
                loopname = blockdata['loopname']
            except KeyError:
                warn("Internal Error: missing blockdata")
                exit(-1)

        if isloopblock:
            try:
                loop = self.loops[loopname]
                i    = 0
            except KeyError, keyname:
                warn("You tried to access the loop %s, but but that loop is unknown. Loop execution aborted" % keyname)
                return None
        else:
            loop = [self.template] # just a dummy with one entry

        for i in xrange(len(loop)): # go through the iterations of the loop (1 iteration if it's not a loop)
            if isloopblock:
                # we need to manually keep track of iterations in loops, and block must be reopened for each iteration
                self.loops[loopname].iteration = i
                block.reopen()
            while True: # go through the lines of the block
                line = block.readline()
                self._replacements = {}
                if not line:
                    break # done with the block
                comments = self._rx_comment.findall(line) + self._rx_comment2.findall(line)
                if len(comments) > 0:
                    for comment in comments:
                        match_var       = self._rx_var.match(comment)
                        match_startloop = self._rx_startloop.match(comment)
                        match_loopvar   = self._rx_loopvar.match(comment)
                        match_endloop   = self._rx_endloop.match(comment)
                        match_if        = self._rx_if.match(comment)
                        match_else      = self._rx_else.match(comment)
                        match_endif     = self._rx_endif.match(comment)

                        if match_var:
                            if self._activeoutput: # no use doing all the work if there's not going to be any output
                                try:
                                    varname = match_var.group(1)
                                    replacement = self._varreplacements[varname]
                                    self._replacements[comment] = replacement
                                except KeyError, keyname:
                                    warn("You tried to replace %s, but there is no entry in the replacement table. The marker is left unchanged" % keyname)

                        elif match_startloop:
                            if self._activeoutput:
                                subblock = LoopLineBlock()
                                while True: # search for end of loop
                                    blockline = block.readline()
                                    if not blockline:
                                        raise TemplateProcessorIllegalLoopMarkerException( \
                                            "The subloop '%s' does not seem to end" % match_startloop.group(1))
                                    match_endloop = self._rx_endloop.search(blockline)
                                    # are the loopnames the same?
                                    if match_endloop and match_startloop.group(1) == match_endloop.group(1):
                                            line = "" # drop that line from the output
                                            break
                                    else:
                                        subblock.append(blockline)
                                self._handleblock( block = subblock, loopname = match_startloop.group(1) )

                        elif match_loopvar:
                            if isloopblock:
                                if self._activeoutput:
                                    try:
                                        loopvar_loopname = match_loopvar.group(1)
                                        loopvarname      = match_loopvar.group(2)
                                        iteration = self.loops[loopvar_loopname].iteration
                                        replacement = self.loops[loopvar_loopname].get(iteration, loopvarname)
                                        if not isinstance(replacement, basestring):
                                            if replacement is None:
                                                warn("The replacement for the loop variable %s in the loop %s was returned as 'None'. This probably means that the variable could not be found by the loop handling function, or that there is some other error in the function. The replacement will be set to ''." % (loopvarname, loopvar_loopname))
                                                replacement = ''
                                            else:
                                                warn("The replacement for the loop variable %s in the loop %s is not a string. We'll try to convert it." % (loopvarname, loopvar_loopname))
                                                try:
                                                    replacement = str(replacement)
                                                except:
                                                    warn("Can't convert the replacement for the loop variable %s in the loop %s to a string. It will be set to ''." % (loopvarname, loopvar_loopname))
                                        self._replacements[comment] = replacement
                                    except KeyError, keyname:
                                        warn("You tried to replace %s, but there is no entry in the loop replacement table for that loop name. The marker is left unchanged" % keyname)
                            else: # no loopvars allowed outside a loop
                                raise TemplateProcessorIllegalLoopMarkerException(\
                                    "The marker '%s' is outside of a loop" % comment)

                        elif match_endloop:
                            # mustn't be there: this match should only occur in the loop handling
                            raise TemplateProcessorIllegalLoopMarkerException(\
                                "The marker '%s' tries to end a loop that is not open" % comment)

                        elif match_if:
                            self._if_stack.append(self._activeoutput)
                            if self._activeoutput:
                                expression = match_if.group(1)
                                # wrap the expression into a function for evaluation
                                # having our own function gives us local scope for the variables
                                evalfunction = 'def evalfunction():\n'
                                for name in self._varreplacements: # first, do the simple variables
                                    if name in expression:
                                        evalfunction = evalfunction + \
                                        '    ' + name + ' = "' + \
                                        (self._varreplacements[name]).replace("\\", "\\\\").replace('"', r'\"') + \
                                        '"\n'
                                if isloopblock:
                                    for lpname in self.loops.keys(): # handle loopnames
                                        if lpname in expression:
                                            # fake the loopname into the local namespace as an object
                                            evalfunction = evalfunction + '    ' + lpname + \
                                                ' = AttributeHolder()\n'
                                        # look for strings in the form "lpname.varname"
                                        for lpvar in re.findall(lpname + r'\.[A-Za-z0-9_]+', expression):
                                            (lpvar_loopname, lpvar_varname) = lpvar.split(".")
                                            try:
                                                lpvar_iteration = self.loops[lpvar_loopname].iteration
                                                lpvar_replacement = \
                                                    self.loops[lpvar_loopname].get(lpvar_iteration, lpvar_varname)
                                            except Exception:
                                                pass
                                            else:
                                                evalfunction = evalfunction + '    ' + lpvar +\
                                                    " = \"" + lpvar_replacement.replace('"', '\\"') +"\"\n"
                                evalfunction = evalfunction + '    return (' + expression + ')\n'
                                try:
                                    evalfunction_code = evalfunction # copy for debug purposes
                                    # make evalfunction available as callable function
                                    exec(evalfunction)
                                    b = evalfunction()
                                    # b is now whatever the expression evaluated to with variable replacements
                                    if not isinstance(b, bool):
                                         warn("There's something wrong with the expression >%s<. It didn't evaluate to a boolean value. Evaluation forced to 'False'" % expression)
                                         warn("The evalfunction was:\n%s" % evalfunction_code)
                                         b = False
                                except Exception ,args:
                                    warn("There's something wrong with the expression >%s<:" % (expression))
                                    warn("The evalfunction was:\n%s" % evalfunction_code)
                                    warn(args)
                                    warn("Evaluation forced to 'False'")
                                    b = False
                                self._activeoutput = b
                                line = "" # drop the line

                        elif match_else:
                            outeractive = self._if_stack.pop() # just a peek
                            if outeractive:
                                self._activeoutput = not self._activeoutput
                            line = "" # drop the line
                            self._if_stack.append(outeractive)

                        elif match_endif:
                            self._activeoutput = self._if_stack.pop()
                            line = "" # drop the line

                    for (string, replacement) in self._replacements.items():
                        line = line.replace(string, replacement)
                if self._activeoutput: self._outfile.write(self.indent + line)
