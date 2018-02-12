def ipv4parse(ipraw,ipv4,nmask):
	octcount = 0
	subs =''
	cidr = 0
	for x in range(0, len(ipraw)):
		if (ipraw[x] >= '0' and ipraw[x] <= '9'):
			subs = subs + ipraw[x]
			ipv4[octcount] = int(subs)
		if (ipraw[x] == '.' or ipraw[x] == '/'):
			subs = ''
			octcount = octcount + 1
	#print(ipv4)
		cidr = ipv4[4]
	print ("CIDR = ",cidr)
	if(cidr == 32):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	if(cidr == 31):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 30):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 252;
	if(cidr == 29):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 248;
	if(cidr == 28):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 240;
	if(cidr == 27):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 128;
	if(cidr == 26):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 192;
	if(cidr == 25):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 24):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 0;
	if(cidr == 23):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 22):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 21):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 20):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 19):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 18):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 17):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 16):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 15):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 14):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 13):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 12):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 11):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 10):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 9):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 8):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 7):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 6):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 5):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 4):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 3):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 2):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 1):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 0):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;			
	return ipv4, nmask

def main():
	ipv4 = [-1,-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	#print(ipv4,end='')
	#print(nmask)
	print ('Input an ip as follows 192.168.1.1/24')
	ipraw = input("ip: ")
	#print (ipraw,' ',end='')
	print("**************************")
	ipv4,netmask = ipv4parse(ipraw,ipv4,nmask)
	print(ipv4,end='')
	print(nmask)
	
main()


