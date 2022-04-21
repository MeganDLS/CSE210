"""
CSE210 W01: 
A game of Tic Tac Toe
Megan De Leon
"""

"""WELCOME"""
print("\n \033[3;32;43m  Welcome to Tic Tac Toe  \n") 

"""USERNAMES"""
"""Get usernames"""
def assign_names():
    pass


"""Grid lines defaults"""
def create_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def display_board(board):
    print(f"""
    {board[0]}|{board[1]}|{board[2]}
    -+-+-
    {board[3]}|{board[4]}|{board[5]}
    -+-+-
    {board[6]}|{board[7]}|{board[8]}
    """)

def edit_board(board, sign):
    square = int(input(sign + " turn to choose a square (1-9): "))
    board[square - 1] = sign
    print(board)    

def change_sign(sign):
    sign = "X" if sign == "O" else "O" 
    print("Winner, Winner!")
    return sign

def is_game_over(board):
    if (board[0] == board[1] == board[2]
    or board[3] == board[4] == board[5]
    or board[6] == board[7] == board[8]
    or board[0] == board[3] == board[6]
    or board[1] == board[4] == board[7]
    or board[2] == board[5] == board[8]
    or board[0] == board[4] == board[8]
    or board[6] == board[4] == board[2]):
        return True
    return False


def main():
    username = input("   Enter P1 Username: ")
    print(" Hello, " + username + "! You are X's")
    print (" ")
    username2 = input("   Enter P2 Username: ")
    print(" Hello, " + username2 + "! You are O's")
    sign = "X"
    board = create_board()
   
    while not is_game_over(board):
        display_board(board)
        edit_board(board, sign)
        sign = change_sign(sign)

    answer = input("\n Would you like to play again? y/n ")
    if answer == "y": 
        print(" Yes!")
        main()
        print("")    
    else:
        print(" Good game. Thanks for playing!")
        print("")

if __name__ =="__main__":
    main()
   