#Question Link: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

'''
Question:
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too
low, too high, or exactly right.
'''

import random

ask_game = "Yes"
ask_guess = "Yes"

while ask_game == "Yes":
    num = random.randint(1,9)
    #print("Guessed number = ", num)
    count = 1
    
    while ask_guess == "Yes":
        guess = int(input("Guess a number between 1 and 9 inclusively: "))
    
        difference = num - guess
    
        if num >= guess: 
            if difference >= 5:
                print("You guessed too low!")
            elif difference == 0:
                print("You guessed it exactly! Congratulations!")
                ask_guess = "No"
                print("You guessed in ", count," many attempts.")
            else:
                print("Your guess is near.")  
        else: # num < guess
            if difference <= -5:
                print("You guessed too high!")
            else:
                print("Your guess is near.")
        
        if difference != 0:
            ask_guess = input("Would you like to guess again? (Yes/No): ")
        count = count + 1
            
    ask_game = input("Would you like to restart? (Yes/No): ")
    if ask_game == "Yes":
        ask_guess = "Yes"

else:
    print("Thank You for playing. Have a great day!")

