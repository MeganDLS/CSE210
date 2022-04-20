"""CSE210 W01: A game of Tic Tac Toe"""
__author__ = "Megan De Leon"

"""Get usernames"""    
username = input("Enter P1 username: ")
print("Hello, " + username + "! You are X's")
print (" ")
username2 = input("Enter P1 username: ")
print("Hello, " + username2 + "! You are O's")


# name = ""
# player = ""
"""Get usernames"""    
# def user_names(name, player):
#     print("Hello, " + name + "! You are " + player + "'s")
#     p1 = "X"
#     p2 = "O"
#     users = {}
#     k = 0
#     while k < 2:
#         key = input("What is your name? ")
#         value = p1
#         users[key] = value
#         k += 1
#         if k == 1:
#             user_names(key, p1)
#         elif k == 2:
#             user_names(key, p2)       
#             print ("Here is the grid, Good Luck!" + users)
# print("Hello, " + username + "! You are X's")
# print (" ")
# username2 = input("Enter P1 username: ")
# print("Hello, " + username2 + "! You are O's")

"""Draw a Grid"""                          
def grid():
    divider = "-+-+-"
    print (" ")
    print ("1|2|3")
    print (divider)
    print ("4|5|6")
    print (divider)
    print ("7|8|9")

# nums = [] #empty list
# for i in range(3): #start at 0
#     nums.append([]) #still empty
#     for j in range(1, 4): # j starts at 1
#         nums[i].append(j) #back and forth to add 1, 2, and 3 to the original list - go back to beginning of i loop to start at 1 to have three sets
# print("select a number:")
# print(nums)

#Or reuse key from dictionary? for usernames.

# """Loop for input 3x"""
# print (" ")
# x = 0
# while x < 9:
#     """Get input from Player 1"""
#     move1 = input("X's choose a number: ")
#     if move1 == 1
"""Get input from Player 2"""
print ("O's choose a number: ")

def main():
    grid()
    answer = input("Would you like to play again? y/n")
    if answer == "y": 
        print("Yes!") #how to start over?
        print("")    
    else:
        print("Good game. Thanks for playing!")

if __name__ =="__main__":
    main()
   