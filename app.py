# Rock Paper Scissors Project

# Get Player's choice
player_choice = input("Choose one(rock, paper, scissors): ").upper()

# Create list of choices 
choices = ["rock", "papesr", "scissors"]

# Verify player choice
if player_choice not in choices:
    print("Invalid choice. Please pick a valid choice(rock, paper, scissors): ")

# Import Random module.
import random

# Get computer's choice
computer_choice = random.choice(choices)

# Define the game
if ( 
    (player_choice == "rock" and computer_choice == "scissors") or
    (player_choice == "paper" and computer_choice == "rock") or
    (player_choice == "scissors" and computer_choice == "rock")
    
): 
    print(f'You win. The computer choose {computer_choice}')
elif player_choice == computer_choice:
    print(f'Draw. The computer chose {computer_choice}')



    



    




