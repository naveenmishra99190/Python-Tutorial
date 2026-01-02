# GUESS THE NUMBER

import random 

target = random.randint(1, 100)

while True:
    userChoice = (input("Guess the target or Quit(Q) : "))
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger number")
    else:
        print("your number was too big. Take a smaller number")    

print("--------GAME OVER--------")