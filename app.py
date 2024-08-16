# Rock Paper Scissors Project

# Get Player's choice
player_choice = input("Choose one(rock, paper, scissors): ").upper()

# import random
import random

# To get computer choice, we must create a list of choices for the computer to choose from.
choices = ["rock", "paper", "scissors"]

# Get computer's choice
computer_choice = random.choice(choices)

# Define the game
if ( 
    (player_choice == "rock" and computer_choice == "scissors") or
    (player_choice == "paper" and computer_choice == "rock") or
    (player_choice == "scissors" and computer_choice == "rock")
    
): 
    print("You Win!")
else:
    print("You Lose!")


    



    




