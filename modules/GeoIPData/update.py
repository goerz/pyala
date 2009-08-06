#!/usr/bin/python
# run this script to update the GeoIP database
import urllib
import gzip
import os

url = "http://www.maxmind.com/download/geoip/database/GeoIP.dat.gz"
file = "GeoIP.dat.gz"

# download the file
print "Downloading GeoIP.dat.gz"
urllib.urlretrieve(url, file)

# unpack the file
print "Unpacking to GeoIP.dat"
infile = gzip.GzipFile(file, "rb")
outfile = open("GeoIP.dat", "wb")

data = infile.read()
outfile.write(data)

infile.close()
outfile.close()

os.remove(file)

print "Done."
print "The GeoIP Database was updated"
