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

def get_user_name():
    player1 = input("Enter your name, player 1: ")
    user1 = {"name":player1, "symbol":"X"}
    player2 = input("Enter you name, player 2: ")
    user2 = {"name":player2, "symbol":"O"}
    return user1,user2

def get_user_input(board):
    while True:
        row = -1
        column = -1
        while row < 0 or row > 2:
            row = input("Enter a row (0-2): ")
            row = int(row)
            if row > 2 or row < 0:
                print("Invalid row number entered")
        while column < 0 or column > 2:
            column = input("Enter a column (0-2): ")
            column = int(column)
            if column > 2 or column < 0:
                print("Invalid column number entered")
        if board[row][column] == " ":

            return row, column
        else:
            print("Sorry, this spot is already taken, please try another spot")

def placing_character(character,board,row,column):
    if board[row][column] == " ":
        board[row][column] = character

def toggle_user(user1,user2,current_user):
    if current_user == user1:
        return user2
    return user1

def check_rows(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
    return False
def check_column(board):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    return False
def check_diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True 
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def main():
    board = create_board()
    user1,user2 = get_user_name()
    current_user = user1
    isWinner = False
    moves  = 0
    printing_board(board)
    while not isWinner and moves < 9:
        print("current user is",current_user["name"],"and symbol:",current_user["symbol"])
        row, column = get_user_input(board)
        board[row][column] = current_user["symbol"]
        moves += 1
        isWinner =  check_column(board) or check_rows(board) or check_diagonal(board)
        print("check passed1")
        if isWinner == True:
            print(current_user["name"],"won the game")
        else:
            current_user  = toggle_user(user1,user2,current_user)
        printing_board(board)

    if not isWinner:
        print("its a draw")
main()