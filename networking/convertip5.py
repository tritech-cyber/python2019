def ipv4parse(ipraw,ipv4,netmask):
	octcount = 0
	charcount = 0
	substring =''
	for x in range(0, len(ipraw)):
	#print(ipraw[x],'-', end='')
	if (ipraw[x] >= '0' and ipraw[x] <= '9'):
		subs = subs + ipraw[x]
		ipv4[octcount] = int(subs)
	if (ipraw[x] == '.' or ipraw[x] == '/'):
		#print(' esl ', end='')
		print(ipraw[x],' ', end='')
		#print(octcount,' ',end='')
		#ipv4[octcount] = int(subs)
		subs = ''
		octcount = octcount + 1
	return ipv4, netmask


def main():
	ipv4 = [-1,-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	print ('Input an ip as follows 192.168.1.1/24')
	ipraw = input("ip: ")
	print (ipraw,' ',end='')
	print("**************************\n")
	ipv4, netmask = ipv4parse((ipraw,ipv4,netmask)
	print(ipv4)
	print(netmask)
	
main()



