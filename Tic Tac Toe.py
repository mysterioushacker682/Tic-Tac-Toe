print("Hey! Lets play Tic Tac Toe!")

def create_row():
    row = []
    for j in range(3):
        row.append(' ')
    return row

def create_board():
    board = []
    for i in range(3):
        row = create_row()
        board.append(row)
    return board

def printing_board(board):
    for k in range(3):
      print(board[k][0] + " | " + board[k][1] + " | " + board[k][2])
      if k < 2:
        print("--+---+--")

def main():
    board = create_board()
    printing_board(board)
    
main()