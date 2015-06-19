import urllib2
import re
num = "12345"
i = 1
while True:
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
	response = urllib2.urlopen(url)
	html = response.read()
	#print html
	num = ''.join(re.findall('[1-9]',html))
	print i, " " + num
	i = i + 1