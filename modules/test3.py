from ApacheLogParser import *
from visit import *
import re

testfile = r'/home/goerz/public_html/logs/access.log.2006-07.gz'

alp = ApacheLogParser(testfile)
alp.compressed = True
#visits = VisitManager()
#alp.add_excludepattern(('hostname', re.compile(r'msnbot')))
#alp.add_excludepattern(('file', re.compile(r'/images/')))
#alp.add_excludepattern(('file', re.compile(r'abiz')))
#alp.add_includepattern(('hostname', re.compile(r'tlnk')))

i = 0
for x in alp:
    print x.hostname


#print "\n\nSummary:"
#print "Accepted Lines     : " + str(alp.acceptedlines())
#print "Rejected Lines     : " + str(alp.rejectedlines())
#print "Not parsable Lines : " + str(alp.notparsablelines())
#print "Total Lines        : " + str(alp.totallines())
