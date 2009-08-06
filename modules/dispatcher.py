from ApacheLogParser import *

class PPCloneDispatcher:
    def __init__(self):
        self.parser = ApacheLogParser()
        self.components = {
            'parser'   : ApacheLogParser(),
            'detailed' : None,
            'time'     : None,
            'global'   : None
        }
        self.optdirections ={ # what to do with an option
            'name' : 'code'
        }
        self.options = {}
        self.outdir = ""
    def setoption(self):
        pass
    def add_includepattern(self):
        pass
    def add_excludepattern(self):
        pass
    def run(self):
        pass
        # pull from parser, and push to components