import urllib2
import re

# Python Challenge
# 4
# Harsha Ashokan Copparam
# 19 June 2015
#


num = "12345"
i = 1
f = open("out.txt","w")
for i in range(1,400):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
	response = urllib2.urlopen(url)
	html = response.read()
	#print html
	num = ''.join(re.findall('[1-9]',html))