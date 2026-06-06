
"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choise = input("Enter your choise = Rock , Paper, Scissor = ")
com_choise = random.choice(item_list)

print(f"User choise : {user_choise} , Computer choise : {com_choise}")

if user_choise == com_choise:
    print("Match is a tie")

elif user_choise == "Rock":
    if com_choise == "Paper":
        print("Paper covers Rock = compter win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choise == "Paper":
    if com_choise == "Rock":
        print("Paper covers rock = You win")
    else:
        print("Scissor smashes paper = computer win")

elif user_choise == "Scissor":
    if com_choise == "Rock":
        print("Rock smashes Scissor = computer win")
    else:
        print("Scissor smashes paper = user win")