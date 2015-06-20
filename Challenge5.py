import urllib2
import pickle



# Python Challenge
# 4
# Harsha Ashokan Copparam
# 19 June 2015
#

pick_stream = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(pick_stream)
pick_stream.close()
#print data


for item in data:
	print ''.join(i[0] * i[1] for i in item)
