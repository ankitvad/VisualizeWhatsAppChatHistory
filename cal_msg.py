import re
b = open("Ayush.txt","r")
a = open("messages.txt","w")
y = b.readline().decode('utf-8-sig').encode('utf-8')
while y:
	if(y != '\r\n'):
		temp = y.split(": ",2)
		x = temp[2]
		x = re.sub('([\:\;][\)\|\\\/dDOoPp\(\'\"][\(\)DOo]?)','',x)
		x = re.sub('[?\.#_]','',x)
		x = re.sub('[\s]+',' ',x)
		a.write(x+"\n")
	y = b.readline()	