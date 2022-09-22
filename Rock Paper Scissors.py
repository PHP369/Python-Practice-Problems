#Question Link: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

'''
Question:
Make a two-player Rock-Paper-Scissors game.
'''

def main():
    player_1 = input("Hi Player 1. Rock, Paper, Scissors? ")
    player_2 = input("Hi Player 2. Rock, Paper, Scissors? ")

    if player_1 == "Rock" and player_2 == "Paper":
        print("Player 2 wins. Congragulations!")
        ask = input("Do you want to play again? (Yes/No) ")
    
    elif player_1 == "Rock" and player_2 == "Scissors":
        print("Player 1 wins. Congragulations!")
        ask = input("Do you want to play again? ")
    
    elif player_1 == "Paper" and player_2 == "Rock":
        print("Player 1 wins. Congragulations!")
        ask = input("Do you want to play again? ")
    
    elif player_1 == "Paper" and player_2 == "Scissors":
        print("Player 2 wins. Congragulations!")
        ask = input("Do you want to play again? ")
    
    elif player_1 == "Scissors" and player_2 == "Rock":
        print("Player 2 wins. Congragulations!")
        ask = input("Do you want to play again? ")
    
    elif player_1 == "Scissors" and player_2 == "Paper":
        print("Player 1 wins. Congragulations!")
        ask = input("Do you want to play again? ")

    else:
        print("Its a tie!")
        ask = input("Do you want to play again? ")

    while ask == "Yes":
        main()
        break

main()
    
print("Thank You! Have a nice day!")
    

