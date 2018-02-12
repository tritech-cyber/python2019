ipv4 = [-1,-1,-1,-1,-1]
nmask =  [-1,-1,-1,-1]
print ('Input an ip as follows 192.168.1.1/24')
ipraw = input("ip: ")
print (ipraw,' ',end='')
print("**************************\n")
octcount = 0
charcount = 0
subs =''
for x in range(0, len(ipraw)):
	#print(ipraw[x],'-', end='')
	if (ipraw[x] >= '0' and ipraw[x] <= '9'):
		subs = subs + ipraw[x]
		ipv4[octcount] = int(subs)
	if (ipraw[x] == '.' or ipraw[x] == '/'):
		#print(' esl ', end='')
		#print(ipraw[x],' ', end='')
		#print(octcount,' ',end='')
		#ipv4[octcount] = int(subs)
		subs = ''
		octcount = octcount + 1
print(ipv4)
		




