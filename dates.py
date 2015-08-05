me = "Ankit Vadehra:"
you = "Ayush:"

ankit_date = open("ankit_date.txt","w")
ayush_date = open("ayush_date.txt","w")

x = open("Ayush.txt","r")
y = x.readline().decode('utf-8-sig').encode('utf-8')
while y:
	if (me in y):
		temp = y.split(" ",1)
		ankit_date.write(temp[0]+"\n")
	elif (you in y):
		temp = y.split(" ",1)
		ayush_date.write(temp[0]+"\n")
	y = x.readline().decode('utf-8-sig').encode('utf-8')



