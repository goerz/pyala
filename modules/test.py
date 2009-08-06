from ApacheLogParser import *
from DetailedStatComponent import DetailedStatComponent
from TemplateProcessor import TemplateProcessor
from visit import *
import re

testfiles = [
    r'/home/goerz/public_html/logs/access.log.2007-09.tempcopy.gz'
]

TemplateProcessor.overwrite = True

alp = ApacheLogParser()
alp.compressed = True
#alp.add_includepattern(('hostname', re.compile(r'physik.fu-berlin.de')))
alp.add_excludepattern(('hostname', re.compile(r'googlebot.com')))
alp.add_excludepattern(('hostname', re.compile(r'inktomisearch')))
alp.add_excludepattern(('hostname', re.compile(r'phx.gbl')))
alp.add_excludepattern(('hostname', re.compile(r'search.live.com')))
alp.add_excludepattern(('hostname', re.compile(r'crawl.yahoo.net')))
alp.add_excludepattern(('file', re.compile(r'/images/')))
alp.add_excludepattern(('file', re.compile(r'/fortunes/')))
alp.add_excludepattern(('file', re.compile(r'/pagestyle\.css')))
alp.add_excludepattern(('hostname', re.compile(r'pfeffer\.zedat')))

visits = VisitManager()
visits.add_excludepattern(('is_bot', re.compile(r'Yes')))
Visit.html_template = "../templates/visit.html"

detailedstats = DetailedStatComponent()
detailedstats.set_option('outdir', "../output")
detailedstats.set_option('imagedir', 'images/')
detailedstats.set_option('html_template', "../templates/detailed.html")
detailedstats.set_option('html_toc_template', "../templates/detailed_toc.html")
detailedstats.set_option('title', "Detailed Statistics for www.physik.fu-berlin.de/~goerz")
detailedstats.set_option('visits_per_page', 250)

# set class attributes for Visit objects


i = 0
for testfile in testfiles:
    alp.filename(testfile)
    for x in alp:
        visits.add_logline(x)
        if len(visits.visits) > 250:
            for visit in visits.visits:
                i += 1
                detailedstats.register_visit(visit)
            visits.clear_closed()
# finish up
visits.close_open_visits()
for visit in visits.visits:
    detailedstats.register_visit(visit)
visits.clear_all()
detailedstats.finish()


print "\n\nSummary of ApacheLogLineParser:"
print "Accepted Lines     : " + str(alp.acceptedlines())
print "Rejected Lines     : " + str(alp.rejectedlines())
print "Not parsable Lines : " + str(alp.notparsablelines())
print "Total Lines        : " + str(alp.totallines())
