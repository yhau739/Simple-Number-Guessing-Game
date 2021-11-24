x = input("What\'s your name?\n")

x = input("Oh , Hello There! " + x + "\n\nWould you like to play our Mini \"Game\"??  (Press Enter to Continue)\n")

x = input("\nThis Mini Game is called:\n\"Guess The Number(1-100)\"                        (Press Enter to Continue)\n")

x = input("\nRules:\nPlayers Guess the \"Hidden\" \"Random\" Number,\nthey would \"WIN\" if they\'re\"RIGHT!!!\"     (Press "
    "Enter to Continue)\n")

z=input("Are u Ready???\nType \"Yes\" If You\'re Ready & \"NO\" If You\'re Not Interested\n")


import sys
while z != "yes" or z != "no":
    if z.lower() == "yes":
        print("Sure! Here We GOOOO!!!")
        break
        

    elif z.lower() == "no":
        print("Aw,Good Bye")
        sys.exit()
    else:
        z = input("Please Answer my question!")



import random
from time import sleep

#randint to generate random int number stored in a variable 
secret = random.randint(1, 100)

#count is used to record the number of guesses used by the user to guess the correct number 
count = 1
guess_int = None

while guess_int != secret:
    #prompt user for input as a "guess"
    guess = input("\nGuess The Number : ")

    #convert the initial data type(str) into (int)
    guess_int = int(guess)

    #create a distance variable to know how close is the guess with the correct number
    distance = abs(guess_int - secret)
    
    if guess_int == secret:
        print("\nYou're Correct!")
        print("\nYou've used " + str(count) + " Guesses!")
    elif guess_int > secret:
        if distance <= 10:
            print("\nYou're getting closer to the right number!")
        else:
            print("\nTry to guess again \n(Hint: the number should be smaller)")

    elif guess_int < secret:
        if distance <= 10:
            print("\nYou're getting closer to the right number!")
        else:
            print("\nTry to guess again \n(Hint: the number should be larger)")
    


    count += 1

sleep(100)
