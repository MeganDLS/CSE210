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
#    turn("X")

"""Get input from Players"""
"Move 1"
def turn(sign):
    print(" ")
    move1 = input(" " + sign + "'s turn to choose a square (1-9): _")
    if move1 == "1":
        global row1 
        row1 = (" " + sign + "|2|3")
        print(row1)
        print(row2)
        print(row3)
    elif move1 == "2":
        #global row1
        row1 = ("1|" + sign + "|3")
        print(row1)
        print(row2)
        print(row3)
    elif move1 == "3":
        #global row1
        row1 = ("1|2|" + sign)
        print (row1)
        print(row2)
        print(row3)
    elif move1 == "4":
        print(row1)
        global row2
        row2 = (" " + sign + "|5|6")
        print(row2)
        print(row3)
    elif move1 == "5":
        print(row1)
        #global row2
        row2 = ("4|" + sign +"|6")
        print(row2) 
        print(row3)
    elif move1 == "6":
        print(row1)
        #global row2
        row2 = ("4|5|" + sign)
        print(row2)
        print(row3)
    elif move1 == "7":
        print(row1)
        print(row2)
        global row3
        row3 = (" " + sign + "|8|9")
        print(row3)
    elif move1 == "8":
        print(row1)
        print(row2)
        #global row3
        row3 = ("7|" + sign + "|9")
        print(row3)
    elif move1 == "9":
        print(row1)
        print(row2)
        #global row3
        row3 = ("7|8|" + sign)
        print(row3)
    
print("")

def main():
    grid()
    t = 0
    while t < 3:
        turn("X")
        turn("O")
        t += 1
    
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
   