"""CSE210 W01: A game of Tic Tac Toe"""
__author__ = "Megan De Leon"

"""WELCOME"""
print("")
print("\033[3;32;43m  Welcome to Tic Tac Toe  \n") 

"""USERNAMES"""
"""Get usernames"""
username = input("   Enter P1 Username: ")
print(" Hello, " + username + "! You are X's")
print (" ")
username2 = input("   Enter P2 Username: ")
print(" Hello, " + username2 + "! You are O's")

"""GRID"""
"""Grid lines defaults"""
row1 = " 1|2|3"
row2 = " 4|5|6"
row3 = " 7|8|9"

"""Draw a Grid"""                          
def grid():
    divider = "-+-+-"
    print (" ")
    print(row1)
    print (" " + divider)
    print(row2)
    print (" " + divider)
    print(row3)
    turn("X")

"""Get input from Player 1"""
"Move 1"
def turn(sign):
    print(" ")
    move1 = input(" " + sign + "'s turn to choose a square (1-9): _")
    if move1 == "1":
        print(" " + sign + "|2|3")
        print(row2)
        print(row3)
    elif move1 == "2":
        print("1|" + sign + "|3")
        print(row2)
        print(row3)
    elif move1 == "3":
        print("1|2|" + sign)
        print(row2)
        print(row3)
    elif move1 == "4":
        print(row1)
        print(" " + sign + "|5|6")
        print(row3)
    elif move1 == "5":
        print(row1)
        print("4|" + sign +"|6")
        print(row3)
    elif move1 == "6":
        print(row1)
        print("4|5|" + sign)
        print(row3)
    elif move1 == "7":
        print(row1)
        print(row2)
        print(" " + sign + "|8|9")
    elif move1 == "8":
        print(row1)
        print(row2)
        print("7|" + sign + "|9")
    elif move1 == "9":
        print(row1)
        print(row2)
        print("7|8|" + sign)
    
"""Get input from Player 2"""
turn("O")
print("")

def main():
    grid()
    print("")
    answer = input(" Would you like to play again? y/n ")
    if answer == "y": 
        print(" Yes!") #how to start over?
        print("")    
    else:
        print(" Good game. Thanks for playing!")
        print("")

if __name__ =="__main__":
    main()
   