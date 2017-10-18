board = []
for i in range(5):
  board.append(['O'] * 5)

def print_board(board_in):
  for r in range(len(board_in)):
    print board_in[r]
    
    
print print_board(board)
