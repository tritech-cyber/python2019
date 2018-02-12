ipv4 = [0,0,0,0]
nmask =  0
subs =""
print ("Input an ip as follows 192.168.1.1/24")
ipraw = input("ip: ")
#print (ipraw)
#print(len(ipraw))
print("**************************\n")
# notdot 0 is false and 1 is true
gotchar = 0
octcount = 0
charcount = 0
for x in range(0, len(ipraw)):
	print (ipraw[x])
	if (ipraw[charcount] != "."):
		nodot = 1
	else:
		nodot = 0
	if (nodot == 1):
		subs = subs + ipraw[charcount]
		charcount = charcount + 1
	else:
		charcount = 0
	print(int(subs))
	#ipv4[octcount] = int(subs)
	#print(ipv4[octcount])
	octcount = octcount + 1
