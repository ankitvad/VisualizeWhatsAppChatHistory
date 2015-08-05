#ankit_count.csv
#arslan_count.csv
x = open("ankit_message.txt","r")
y = x.read()
a = y.split(", ")
c = open("ankit_count.csv","w")
c.write('\n'.join(a))
c.close()
x.close()

x = open("ayush_message.txt","r")
y = x.read()
a = y.split(", ")
c = open("ayush_count.csv","w")
c.write('\n'.join(a))
c.close()
x.close()
