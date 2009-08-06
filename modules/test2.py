from TopListKeeper import TopListKeeper

top_hostnames = TopListKeeper()

infile = open('hostnames2.txt')

for hostname in infile:
    hostname = hostname.rstrip()
    top_hostnames.add(hostname)

toplist = top_hostnames.toplist_tuple(10)
print "TOP 10"
for item in toplist:
    print "%s:\t\t%s" % item
print ""


toplist = top_hostnames.toplist_tuple(20)
print "TOP 20"
for item in toplist:
    print "%s:\t\t%s" % item
print ""