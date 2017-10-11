import random

def diceroll():
	random.seed()
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	sum = (d1+d2)
	return sum,d1,d2
	
def playgame(bet,cash):
	bet = float(bet)
	sum,d1,d2 = diceroll()  # roll the dice
	print ("[ Di 1 = ", d1,"] Di 2 = ", d2, "] [Di 1 + Di 2 = ", sum, "]")
	if (sum==7 or sum==11):
		cash = cash + bet
		print ("You WON and now have $",end=""),print(cash)
		# if roll is 2,3 or 12 you Lose!
	if(sum==2 or sum==3 or sum==12):
			print("*****")
			cash = cash - bet
			print ("You LOST and now have $",end=""),print (cash)
	else:
		print ('Your POINT is ', sum, ' You must now roll ', sum, ' before you roll a 7 ')
		print ('in order to add to your $', cash, ' cash.')
	return cash

def main():
	while True:
		cash = 1000
		print ("Input a dollar amount to bet less than $",end=""),print(cash)
		bet = input("\t? ")
		cash = playgame(bet,cash)
		print (cash)
if __name__ == '__main__':
	main()
