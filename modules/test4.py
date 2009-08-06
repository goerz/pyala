from RefererAnalyzer import *

testfile = r'referers.txt'

testfile = open(testfile)

ra = RefererAnalyzer()

i = 0
for line in testfile:
    ra.analyze(line)
    ra._debug()