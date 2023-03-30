#! python3

import random

Options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
Rock = [2, 3]
Paper = [0, 4]
Scissors = [1, 3]
Lizard = [1, 4]
Spock = [0, 2]
Computer = None

print("\nPrepare for a game of Rock Paper Scissors Lizard Spock\nYour options are as follows: ", Options)

def play():
    Choice = str(input("Choose your weapon: "))
    Computer = Options[random.randint(0,4)]
    if Options.index(Computer)==Options.index(Choice):
        print("Draw!\n")
    elif Options.index(Computer) in 

play()
