from TemplateProcessor import *

TemplateProcessor.overwrite = True
tp = TemplateProcessor(template = "templates/visit.html")

def loopdata(index, varname):
    if varname == 'iteration':
        return str(index)
    elif varname == 'pagename':
        return 'page' + str(index)
    elif varname == 'time':
        return str(12353212+index)
    elif varname == 'code':
        return '200'


tp.replacements = {
    'begin_time_string' : 'March 12',
    'bot_name' : 'Google',
    'browser' : 'Firefox -- "the best browser"',
    'browsericon' : 'firefox.png',
    'countryextension' : 'DE',
    'countryname' :  'Germany',
    'end_time_string' : 'March 13',
    'from' :  'www.google.com/search',
    'fullbrowser' : 'Firefox 2.0.0.1',
    'hostname' : 'foobar.homeip.net',
    'is_bot' : 'No',
    'os' :  'Linux',
    'osicon' : 'linux.png',
    'user' :  'goerz',
    'search' : 'michael goerz',
    'referer' : 'www.google.com/referer',
    'first_logline' : 'blablub This is a logline',
}
tp.loops = {'pages' : LoopData(length=10, datafunction=loopdata),
            'subloop' : LoopData(length=5, datafunction=loopdata)
           }
tp.output = "outfile.html"

tp.run()
