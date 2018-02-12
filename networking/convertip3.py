ipv4 = [-1,-1,-1,-1,-1]
nmask =  0
subs =''
print ('Input an ip as follows 192.168.1.1/24')
ipraw = input("ip: ")
print (ipraw,' ',end='')
print(len(ipraw))
print("**************************\n")
# notdot 0 is false and 1 is true
gotchar = 0
octcount = 0
charcount = 0
for x in range(0, len(ipraw)):
	print(ipraw[x],' - ', end='')
	if (ipraw[x] >= '0' and ipraw[x] <= '9'):
		subs = subs + ipraw[x]
	else:
		#print(' * ', end='')
		#print(ipraw[x],' ', end='')
		print(octcount,' octcount ',end='')
		ipv4[octcount] = int(subs)
		subs = ''
		octcount = octcount + 1
		#print(ipv4)
print(ipv4)


