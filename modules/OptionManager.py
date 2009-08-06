# -*- coding: utf-8 -*-
import sys

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


class OptionManagerUnknownOptionException(Exception):
    def _init__(self, *args):
        warn("You tried to set a value for a invalid option '%s'." % args[0])

class OptionManagerRuleNotCallableException(Exception):
    def _init__(self, *args):
        warn("Rule is not callable: %s" % args[0])

class OptionManagerTransformNotCallableException(Exception):
    def _init__(self, *args):
        warn("Transformation is not callable:  %s" % args[0])

class OptionManagerOptionNotSetException(Exception):
    def _init__(self, *args):
        warn("The option '%s' is not set." % args[0])

class OptionManagerDoesNotMatchRuleException(Exception):
    def _init__(self, *args):
        warn("The value of option '%s' does not meet the specified rule." % args[0])


# some standard translations / rules
def rule_regex(r):
    """ Generate a boolean match function for the compiled regex r

        The generated function will have one string parameter and will
        return True if the string matches the regex r, False otherwise.
    """
    import re
    if type(r) == type(re.compile("")):
        def f(s):
            try:
                if r.search(s):
                    return True
                else:
                    return False
            except TypeError:
                warn("Option value must be a string. Regex will not match")
                return False
        return f
    else:
        warn("Couldn't compile %s does not seem to be a regex. The rule will always match" % r)
        return lambda s: True

def rule_ensure_dir(d):
    """ Create the path d and return True on success or if the directory
        already exists, return False otherwise.
    """
    import os.path
    try:
        if not os.path.isdir(d):
            os.makedirs(d)
        return True
    except:
        return False

class OptionManager(object):
    """ Manage options

        The OptionsManager will allow you to define option names, rules for
        the object values, and transformations. You will be able to get and
        set option values and it will retain them for you.

        There is one public attribute:
            validoptions []   a list of strings that are valid attributes
                              You must set this to have any functionality

        If you want to use this to manage the options for another class, it
        is advisable to wrap it.
    """
    def __init__(self):
        self.validoptions = []
        self._rules = {}
        self._transforms = {}
        self._options = {}

    def set_option(self, option, value):
        """ Set a known option and return the value the option was set to.

            Set the value of option (which must be in the validoptions list).
            If there are no rules and no transformations defined for that
            option, the option  will be set directly to the value provided.

            If a rule is set for the option, the option will only be set to
            the value if the value matches the rule, otherwise, an exception
            will occur.

            If a transformation is set for the option, the option will be set
            to whatever the transformation of the original value yields. Note
            that in combination with a rule, it is the original value that
            must pass the rule, not the transformed one.
        """
        if option in self.validoptions:
            if self._rules.has_key(option):
                if not self._rules[option](value):
                    raise OptionManagerDoesNotMatchRuleException, option
            if self._transforms.has_key(option):
                value = self._transforms[option](value)
            self._options[option] = value
            return self._options[option]
        else:
            raise OptionManagerUnknownOptionException, option

    def add_list_option(self, option, value):
        """ Add value to the list that is associated with the option.

            This works as set_option, except that the option is converted to
            a list and value is appended to that list.

            If the option was previously set with set_option to an oldvalue,
            calling add_list_option(newvalue) will cause the option to be set
            to the list [oldvalue, newvalue]

            If the option was previously set with n calls to add_list_option,
            calling add_list_option(valuem) will cause the option to be set to
            the list [value1, value2, ... valuen, valuem]

            Any added value will have to match the possible rule, and will be
            transformed if applicable
        """
        if option in self.validoptions:
            if self._rules.has_key(option):
                if not self._rules[option](value):
                    warn("The option value does not meet the specified rule. It will not be set.")
                    return None
            if self._transforms.has_key(option):
                value = self._transforms[option](value)
            if not self._options.has_key(option):
                self._options[option] = []
            if not isinstance(self._options[option], list):
                self._options[option] = [self._options[option]]
            self._options[option] = list(self._options[option]) + [value]
            return self._options[option]
        else:
            raise OptionManagerUnknownOptionException, option

    def remove_list_option(self, option, value):
        """ An inverse to add_list_option

            Remove the first occurance of value from the list associated with
            the option. The value will first be transformed, if applicable
        """
        if option in self.validoptions:
            if self._transforms.has_key(option):
                value = self._transforms[option](value)
            if self._options.has_key(option) and isinstance(self._options[option], list):
                try:
                    self._options[option].remove(value)
                except ValueError:
                    warn("%s is not in the list of option %s, so it cannot be removed" % (value, option))
            else:
                raise OptionManagerOptionNotSetException, option
            return self._options[option]
        else:
            raise OptionManagerUnknownOptionException, option

    def get_option(self, option):
        """ Return the value for option, or throw an Exception if option was not set """
        if self._options.has_key(option):
            return self._options[option]
        else:
            raise OptionManagerUnknownOptionException, option

    def del_option(self, option):
        """ Unset the option """
        if self._options.has_key(option):
            del self._options[option]
            return None
        else:
            raise OptionManagerUnknownOptionException, option

    def set_transform(self, option, f):
        """ Set a transformation for an option

            The transformation  f should transform an original value to the
            value the option is actually set to. It has to be a callable
            object that accepts a value as its only input. It must return the
            transformed value.

            You can use this to make conversion, e.g. from string to integer:
                set_transform('opt', int)
        """
        if callable(f):
            if option in self.validoptions:
                self._transforms[option] = f
            else:
                raise OptionManagerUnknownOptionException, option
        else:
            raise OptionManagerTransformNotCallableException

    def set_rule(self, option, f):
        """ Set a rule f for an option.

            The rule must be a callable option the accepts a value as its only
            input, and must return a boolean value, True if the value matches
            the rule, False otherwise.

            This package contains some rule generating functions, e.g.
                set_rule('opt' rule_regex(re.compile('^[0-9]+$')))
        """
        if callable(f):
            if option in self.validoptions:
                self._rules[option] = f
            else:
                raise OptionManagerUnknownOptionException, option
        else:
            raise OptionManagerTransformNotCallableException
