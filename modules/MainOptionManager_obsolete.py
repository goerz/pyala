# -*- coding: utf-8 -*-
import sys

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")



class ApacheLogParserOptions(object):
    """ Submanager for the ApacheLogParser component """
    _validoptions = []
    def setoption(self, option, value):
        pass
    def getoption(self, option):
        pass
    def pass_on(self, alp_object):
        pass



class MultiHandler(object):
    """ The submanager for all options that have effects on multiple components """
    def __init__(self, submanagers):
        self._submanagers = submanagers # passed on from the Option Manager
    def setoption(self):
        pass
    def getoption(self):
        pass



class SetValueProcessor(object):
    """ Provides functions for transforming option value strings to whatever they should be """
    _mappings = {} # optionname->function


class GetValueProcessor(object):
    _translation_mappings = {} # option name to function that creates a string from the object's value (for the getter)



class OptionManager(object):
    """ Manage all option, reads and writes to config file"""
    def __init__(self):
        #_validoptions = [] # all option strings that are understood -- Shouldn't this be _mappings.keys()?
        _rules = {} # regexes for the values
        _mappings = {} # where does the option belong?  optionname -> submanager
                       # Will later be executed as submanager.setoption('option', ValueProcessor.process('option', 'value'))
        _submanagers = {} # sub-handlers for everything
    def setoption(self, option, value):
        pass
    def getoption(self, option):
        pass
    def read_configfile(self, filename):
        pass
    def write_configfile(self, filename):
        pass