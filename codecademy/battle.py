from random import randint 

board = []
for i in range(5):
  board.append(['O'] * 5)

def print_board(board_in):
  for r in range(len(board_in)):
    print (" ".join(board_in[r]))
    

# Add your code below!
def random_row(board_in):
  return randint(0, len(board_in) - 1)
  
def random_col(board_in):
  return randint(0, len(board_in) - 1)
  
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row," ",ship_col)

for turn in range(4):
 
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print ("Congratulations! You sank my battleship!")
		break
	else:
		if guess_row not in range(5) or guess_col not in range(5):
			print ("Oops, that's not even in the ocean.")
		elif board[guess_row][guess_col] == "X":
			print ("You guessed that one already.")
		else:
			print ("You missed my battleship!")
			board[guess_row][guess_col] = "X"
			print ("Turn",turn+1)
		if turn == 3:
			print ("Game Over")
		print_board(board)

####
loops

count = 0

if count <= 9:
  print "Hello, I am an if statement and count is", count

while count <= 9:
  print "Hello, I am a while and count is", count
  count += 1
  
####

loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False

#######

num = 1

while num <=10:  # Fill in the condition
  # Print num squared
  # Increment num (make sure to do this!)
	print num**2
	num +=   1
	
#######


choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
  

