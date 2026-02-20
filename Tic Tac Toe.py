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
'''PART 3: Take Player Input
Ask the player to enter row (0-2) and column (0-2).
Convert input into integers.

Expected Output:

Enter row (0-2): 1
Enter column (0-2): 2'''
def get_user_name():
    player1 = input("enter your name")
    player2 = input("enter you name")
    return player1, player2
def get_user_input():
    row = -1
    print("")
    while row < 0 or row > 2:
        row = input("enter a row (0-2)")
        row = int(row)
    column = -1
    while column < 0 or column > 2:
        column = input("enter a column (0-2)")
        column = int(column)
    return row, column

    

def main():
    board = create_board()
    printing_board(board)
    player1, player2 = get_user_name()
    row, column = get_user_input()

main()