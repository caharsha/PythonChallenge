from string import maketrans

# Python Challenge
# 2
# Harsha Ashokan Copparam
# 19 June 2015
#

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
temp = list(str)
newtemp = []
for s in temp:
	if(s == 'y'):
		newtemp.append('a')
	elif(s == 'z'):
		newtemp.append('b')
	elif(s.isalpha()):
		newtemp.append(chr(ord(s) + 2))
	else:
		newtemp.append(s)
str = ''.join(newtemp)
print str


#using string.maketrans() to do it this time.

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
fr = "abcdefghijklmnoprstuvwxyz"
to = "cdefghijklmnoprstuvwxyzab"
trantab = maketrans(fr,to)
print str.translate(trantab)
