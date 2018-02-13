ipv4 = [-1,-1,-1,-1,-1]
nmask =  [-1,-1,-1,-1]
print ('Input an ip as follows 192.168.1.1/24')
ipraw = input("ip: ")
print (ipraw,' ',end='')
print("**************************\n")
octcount = 0
subs =''
for x in range(0, len(ipraw)):
	if (ipraw[x] >= '0' and ipraw[x] <= '9'):
		subs = subs + ipraw[x]
		ipv4[octcount] = int(subs)
	if (ipraw[x] == '.' or ipraw[x] == '/'):
		subs = ''
		octcount = octcount + 1
print(ipv4)
		




