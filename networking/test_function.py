def fun(a,b,c):
		z = a * b * c
		y = a**b
		return y,z

def main():
	a = 10; b = 20; c = 30;
	print ('Input an ip as follows 192.168.1.1/24')
	y,z = fun(a,b,c)
	print(y,z)
main()


