# save this file as random_int.py
from random import randint
def randlist(r,usedlist,done):
	alpha = ["0","1","2","3","4","5","6","7","8","9","0",")",
				"a","A","b","B,","c","C","d","D","e","E","f",
				"F","g","G","h","H","i","I","j","J","k","K",
				"l","L","m","M","n","N","o","O","p","P","q",
				"Q","r","R","s","S","t","T","u","U","v","V",
				"w","W","x","X","y","Y","z","Z","`","[","]",
				"\\",";","'",",",".","/","~","!","@","#","$",
				"%","^","&","*","(",")","_","+","{","}","|",
				":",'"',"<",">","?"]
	#print (len(alpha))
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	#print (sum)
	if (sum == 94):
		done = True
	return c, usedlist, done # this is belongs to  ranlist(r)
	
def main():
	count = 0
	used = [0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0]
	done = False
	while (done == False):
		r = randint(0,93)
		while (used[r] != 1):
			c,used,done = randlist(r,used,done)
			#print (used)
			print(c,end="")
			count += 1
	print ("\n\n",count," randoms numbers used")
main()


