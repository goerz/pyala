# -*- coding: utf-8 -*-
import gzip
import re
import time
import calendar
import sys

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


def stringdate(epochseconds, pattern = "%a, %d %b %Y %H:%M:%S", offset=0):
    """ Convert epoch seconds (UTC) into a local string
        This is a wrapper around time.strftime

        Optional parameters are 'pattern' and 'offset'
        The default pattern is "%a, %d %b %Y %H:%M:%S".
        The offset describes the timezone, i.e. difference in hours to UTC.
        The standard offset is 0
    """
    return time.strftime(pattern, time.gmtime(epochseconds+offset*3600))

def extract_from_date(epochseconds, offset=0):
    """ Convert epoch seconds (UTC) into a localizd time tuple
        This is a wrapper around time.gmtime()

        Optional parameters are 'pattern' and 'offset'
        The standard pattern is "%a, %d %b %Y %H:%M:%S".
        The offset describes the timezone, i.e. difference in hours to UTC.
        The standard offset is 0
    """
    return time.gmtime(epochseconds+offset*3600)


class ApacheLogParser:
    """ Run through a Apache Log File and returns a ApacheLogLine object for each line

        All input/output should be in ASCII

        There is one instance attribute:
            compressed [False]   input file is compressed with gzip

    """
    _linepattern = re.compile(r"""
            (.*) # hostname
            [ ]
            -
            [ ]
            (.+) # user
            [ ]
            \[(.*)\] # access time
            [ ]
            "[A-Z]+ (.*) HTTP.*" # file
            [ ]
            ([0-9-]+) # code
            [ ]
            ([0-9-]+) # size
            [ ]
            "(.*)" # referer
            [ ]
            "(.*)" # browser
            [ ]*
            """, re.X);
    _apachetimepattern = re.compile(r"""
            (?P<day>\d{2})/
            (?P<month>\w{3})/
            (?P<year>\d{4}):
            (?P<hour>\d{2}):
            (?P<minute>\d{2}):
            (?P<second>\d{2})[ ]
            (?P<zone>(\+|-)\d{2})00""", re.X);
    _monthnames = {'jan':1, 'feb':2, 'mar':3, 'apr': 4, 'may': 5, 'jun': 6,
                   'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':10};

    def __init__(self, filename=""):
        self._includepatterns = []
        self._excludepatterns = []
        self._acceptedlines = 0
        self._rejectedlines = 0
        self._notparsable = 0
        self._totallines = 0
        self._filename = filename
        self._filehandle = None
        self._codetranslator = ApacheCodeTranslator()
        self.compressed = False

    def acceptedlines(self):
        """ Return the number of accepted lines """
        return self._acceptedlines
    def rejectedlines(self):
        """ Return the number of rejected lines """
        return self._rejectedlines
    def notparsablelines(self):
        """ Return the number of lines that were not parsable """
        return self._notparsable
    def totallines(self):
        """ Return the number of total processed lines """
        return self._totallines
    def __iter__(self):
        return self

    def filename(self, filename):
        """ Set the filename of the log file that is to be parsed"""
        if not self._filehandle is None:
            self._filehandle.close()
            self._filehandle = None
        self._filename = filename


    def settimepattern(self, pattern):
        """ Set a non-standard pattern for the time format in the logfile

        pattern must be a regular expression object. The standard pattern is:

        re.compile(r'''
            (?P<day>\d{2})/
            (?P<month>\w{3})/
            (?P<year>\d{4}):
            (?P<hour>\d{2}):
            (?P<minute>\d{2}):
            (?P<second>\d{2})[ ]
            (?P<zone>(\+|-)\d{2})00''', re.X)

         The pattern that your provide must define the same named groups.
        """
        self._apachetimepattern = pattern

    def parsedate(self, timestring):
        """ Convert a apache time string to a tuple of UTC epoch seconds and a server time offset """
        timematch = self._apachetimepattern.match(timestring)
        if timematch:
            day     = int(timematch.group("day"))
            try:
                month   = self._monthnames[timematch.group("month").lower()]
            except KeyError:
                month   = int(timematch.group("month"))
            year    = int(timematch.group("year"))
            hour    = int(timematch.group("hour"))
            minute  = int(timematch.group("minute"))
            second  = int(timematch.group("second"))
            zone    = int(timematch.group("zone"))
            result = int(calendar.timegm((year,month,day,hour,minute,second,0,0,-1)))
            result -= zone*3600 # take the zone of the log file into account
            return (result, zone)
        else:
            warn("the string '%s' could not be parsed" % timestring)
        return (0,0)



    def decodeline(self, line):
        """ Converts a line from an Apache log file into an ApacheLogLine object"""
        result = ApacheLogLine()
        result.full_line = line
        linepatternmatch = self._linepattern.match(line)
        if linepatternmatch:
            result.hostname = linepatternmatch.group(1)
            result.user = linepatternmatch.group(2)
            if result.user == '-':
                result.user = ''
            (result.accesstime_seconds, result.serveroffset) = self.parsedate(linepatternmatch.group(3))
            result.accesstime_string = stringdate(result.accesstime_seconds, offset=result.serveroffset)
            result.file = linepatternmatch.group(4)
            result.code = linepatternmatch.group(5)
            result.code_description = self._codetranslator.get_description(result.code)
            result.size = linepatternmatch.group(6)
            if result.size == '-':
                result.size = 0
            result.referer = linepatternmatch.group(7)
            if result.referer == '-':
                result.referer = ''
            result.browser = linepatternmatch.group(8)
        else:
            self._notparsable += 1
            warn("The line '%s' could not be parsed" % line)
            return None
        if self._line_fits_pattern(result):
            self._acceptedlines += 1
            return result
        else:
            self._rejectedlines += 1
            return None

    def next(self):
        """ Returns the ApacheLogLine object for the next line in the logs that passes
        the filters. Throws a StopIteration exception if there are no more lines in the
        log file.
        """
        result = None
        while result is None:
            if self._filehandle is None:
                if self.compressed:
                    self._filehandle = gzip.GzipFile(self._filename, "r")
                else:
                    self._filehandle = open(self._filename, "r")
            line = self._filehandle.next()
            line = line.rstrip()
            self._totallines += 1
            result = self.decodeline(line)
        return result

    def add_includepattern(self, patterntuple):
        """ Add an include filter.

            Lines will only be accepted if they match this filter

            patterntuple consists of
            ('fieldname' , re.compile('regex'))
            with 'fieldname' being a valid attribute of a ApacheLogLine
        """
        if isinstance(patterntuple, tuple) and isinstance(patterntuple[0], str):
            self._includepatterns.append(patterntuple)
        else:
            warn("Include patterns must be tuples of a field name and a compiled regex.")
    def add_excludepattern(self, patterntuple):
        """ Add an exclude filter.

            Lines will be rejected if they match this filter

            patterntuple consists of
            ('fieldname' , re.compile('regex'))
            with 'fieldname' being a valid attribute of a ApacheLogLine
        """
        if isinstance(patterntuple, tuple) and isinstance(patterntuple[0], str):
            self._excludepatterns.append(patterntuple)
        else:
            warn("Exclude patterns must be tuples of a field name and a compiled regex.")
    def clear_includepatterns(self):
        """ Delete all include patterns. """
        self._excludepatterns = []
    def clear_excludepatterns(self):
        """ Delete all exclude patterns """
        self._excludepatterns = []

    def _line_fits_pattern(self, logline):
        """ Tests if a ApacheLogLine passes the include- and exclude-patterns"""
        for (fieldname, pattern) in self._excludepatterns:
            try:
                m = pattern.search(str(logline.__dict__[fieldname]))
            except AttributeError:
                warn("Exclude patterns must be tuples of a field name and a compiled regex.")
                warn("The object that you provided as a regex seems not to have a 'search' method")
                exit(-1)
            except KeyError:
                warn("You tried to filter for a field that doesn't exist")
                m = False
            if m:
                return False
        if len(self._includepatterns) == 0:
            return True # no includepatterns means 'accept everything'
        for (fieldname, pattern) in self._includepatterns:
            try:
                m = pattern.search(str(logline.__dict__[fieldname]))
            except AttributeError:
                warn("Exclude patterns must be tuples of a field name and a compiled regex.")
                warn("The object that you provided as a regex seems not to have a 'search' method")
                exit(-1)
            except KeyError:
                warn("You tried to filter for a field that doesn't exist")
                m = False
            if m:
                return True
        return False




class ApacheLogLine:
    """ Represent a single line in a Apache log file, split up in fields

        The fields are:
            full_line               the original log line
            hostname                hostname
            user                    .htaccess username, if any
            accesstime_seconds      time of access in UTC epoch seconds
            accesstime_string       a string representation, currently in server time
            file                    the file that was access
            code                    the apache return code
            code_description        a description of the apache return code
            size                    the number of bytes that were transmitted
            referer                 the referer string
            browser                 the browser string
            serveroffset            the offset of the server's time zone to UTC, in hours
    """
    def __init__(self):
        self.full_line = ''
        self.hostname = ''
        self.user = ''
        self.accesstime_seconds = 0
        self.accesstime_string = 0
        self.file = ''
        self.code = 0
        self.size = 0
        self.referer = ''
        self.browser = ''
        self.serveroffset = 0
    def __str__(self): # for debugging
        result = str(type(self)) + "\n"
        for attribute in self.__dict__.keys():
            result =  result + "    " + attribute + ": " + str(self.__dict__[attribute]) + "\n"
        return result


class ApacheCodeTranslator(object):
    """ Translator for Apache status/error codes to descriptions"""

    message = {
    '100' : 'Continue',
    '101' : 'Switching Problems',
    '102' : 'Processing',
    '200' : 'OK',
    '201' : 'Created',
    '202' : 'Accepted',
    '203' : 'Non-Authorative Information',
    '204' : 'No Content',
    '205' : 'Reset Content',
    '206' : 'Partial Content',
    '300' : 'Multiple Choices',
    '301' : 'Moved Permanently',
    '302' : 'Moved Temporarily',
    '303' : 'See Other',
    '304' : 'Not Modified',
    '305' : 'Use Proxy',
    '400' : 'Bad Request',
    '401' : 'Authorization Required',
    '402' : 'Payment Required (not used yet)',
    '403' : 'Forbidden',
    '404' : 'Not Found',
    '405' : 'Method Not Allowed',
    '406' : 'Not Acceptable (encoding)',
    '407' : 'Proxy Authentication Required',
    '408' : 'Request Timed Out',
    '409' : 'Conflicting Request',
    '410' : 'Gone',
    '411' : 'Content Length Required',
    '412' : 'Precondition Failed',
    '413' : 'Request Entity Too Long',
    '414' : 'Request URI Too Long',
    '415' : 'Unsupported Media Type',
    '416' : 'Request Range Not Satisfiable',
    '417' : 'Expectation Failed',
    '422' : 'Unprocessable Entity',
    '423' : 'Locked',
    '424' : 'Failed Dependancy',
    '425' : 'No Code',
    '500' : 'Internal Server Error',
    '501' : 'Not Implemented',
    '502' : 'Bad Gateway',
    '503' : 'Service Unavailable',
    '504' : 'Gateway Timeout',
    '505' : 'HTTP Version Not Supported',
    '506' : "Variant Also Negotiates",
    '507' : "Insufficient Sotrage",
    '510' : "Not Extended"}

    def get_description(self, code):
        """ Get the description belonging to code """
        try:
            return self.message[str(code)]
        except KeyError:
            return "Unknown (" + str(code) + ")"