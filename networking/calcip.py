def hostips(cidr,netid,bcastip,firstip,lastip):
	cidr = int(cidr)
	#print (cidr)
	for i in range(0,4):
		firstip[i] = netid[i] 
		lastip[i] = bcastip[i]
		firstip[3] = firstip[3]+1
		lastip[3] = lastip[3]-1
	
	return firstip,lastip
	
def netidparse(ipv4,nmask,netid):
	for i in range(0,4):
		#print('i ',i)
		netid[i] = (ipv4[i] & nmask[i]) 
	return netid

def bcastparse(nmask,netid,bcastip):
	imask = [-1,-1,-1,-1]
	for i in range(0,4):
		imask[i] = ~nmask[i]&255
		bcastip[i] = netid[i]^imask[i]
	return bcastip

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
		print(ipv4)
		cidr = int(ipv4[4])
	print ("CIDR = ",cidr)
	if(cidr == 32):
		nmask = [255,255,255,255]
	if(cidr == 31):
		nmask = [255,255,255,254]
	if(cidr == 30):
		nmask = [255,255,255,252]
	if(cidr == 29):
		nmask = [255,255,255,248]
	if(cidr == 28):
		nmask = [255,255,255,240]	
	if(cidr == 27):
		nmask = [255,255,255,224]	
	if(cidr == 26):
		nmask = [255,255,255,196]
	if(cidr == 25):
		nmask = [255,255,255,128]
	if(cidr == 24):
		nmask = [255,255,255,0]
	if(cidr == 23):
		nmask = [255,255,254,0]	
	if(cidr == 22):
		nmask = [255,255,252,0]	
	if(cidr == 21):
		nmask = [255,255,248,0]
	if(cidr == 20):
		nmask = [255,255,240,0]
	if(cidr == 19):
		nmask = [255,255,224,0]
	if(cidr == 18):
		nmask = [255,255,196,0]	
	if(cidr == 17):
		nmask = [255,255,128,0]	
	if(cidr == 16):
		nmask = [255,255,0,0]
	if(cidr == 15):
		nmask = [255,254,0,0]
	if(cidr == 14):
		nmask = [255,252,0,0]
	if(cidr == 13):
		nmask = [255,248,0,0]	
	if(cidr == 12):
		nmask = [255,240,0,0]	
	if(cidr == 11):
		nmask = [255,224,0,0]
	if(cidr == 10):
		nmask = [255,196,0,0]
	if(cidr == 9):
		nmask = [255,128,0,0]
	if(cidr == 8):
		nmask = [255,0,0,0]	
	if(cidr == 7):
		nmask = [254,0,0,0]	
	if(cidr == 6):
		nmask = [252,0,0,0]
	if(cidr == 5):
		nmask = [248,0,0,0]
	if(cidr == 4):
		nmask = [240,0,0,0]
	if(cidr == 3):
		nmask = [224,0,0,0]	
	if(cidr == 2):
		nmask = [196,0,0,0]	
	if(cidr == 1):
		nmask = [128,0,0,0]
	if(cidr == 0):
		nmask = [0,0,0,0]
			
	return ipv4, nmask

def main():
	ipv4 = [-1,-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcastip = [-1,-1,-1,-1]
	firstip = [-1,-1,-1,-1]
	lastip = [-1,-1,-1,-1]
	print ('Input an IP as follows \n192.168.116.0/27:')
	ipraw = input('              IP: ')
	print('* * * * * * * * * * * * * * * * * * * * * * * * * *')
	ipv4,nmask = ipv4parse(ipraw,ipv4,nmask)
	#print('main ipv4',ipv4)
	cidr = int(ipv4[4])
	netid = netidparse(ipv4,nmask,netid)
	bcastip = bcastparse(nmask,netid,bcastip)
	print('      IP:',ipv4[0],ipv4[1],ipv4[2],ipv4[3])
	print('NET-MASK:',nmask[0],nmask[1],nmask[2],nmask[3])
	print('  NET-ID:',netid)
	print('BCAST-IP:',bcastip)
	print('CIDR:',cidr)
	firstip, lastip = hostips(cidr,netid,bcastip,firstip,lastip)
	print ("HOST RANGE");
	print (firstip,' - ', lastip)
main()

#Subnet Address			Host Range		    				Broadcast Address
#192.168.116.0/27		192.168.116.1 -192.168.116.30		192.168.116.31
#192.168.116.32/27		192.168.116.33 -192.168.116.62		192.168.116.63
#192.168.116.64/27		192.168.116.65 -192.168.116.94		192.168.116.95
#192.168.116.96/27		192.168.116.97 – 192.168.116.126	192.168.116.127
#192.168.116.128/27		192.168.116.129 – 192.168.116.158	192.168.116.159
#192.168.116.160/27		192.168.116.161 – 192.168.116.190	192.168.116.191
#192.168.116.192/27		192.168.116.193 – 192.168.116.222	192.168.116.223
#192.168.116.224/27		192.168.116.225 – 192.168.116.254	192.168.116.255
