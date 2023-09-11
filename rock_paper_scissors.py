# We will write a rock paper scissors game in class - Complete it in this file
import random

player_choice = "rock"
computer_choice = "paper"

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

def check_winner (player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors, You win!"
        else:
            return "paper covers rock, You lose!"
    elif player == "paper":
        if computer == "paper":
            return "paper covers rock, You win!"
        else:
            return "scissors cuts paper, You lose!"
    elif player == "scissors":
        if computer == "scissors":
            return "scissors cuts paper, You win!"
        else:
            return "rock smashes scissors, You lose!"
    
result = check_winner("rock","rock")
print(result)