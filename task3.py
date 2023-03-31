#! python3

import random

Options = ['Rock' , 'Paper', 'Scissors', 'Lizard', 'Spock']
Pairs = {'Rock': [2, 3], 'Paper': [0, 4], 'Scissors': [1, 3], 'Lizard': [1, 4], 'Spock': [0, 2]}

print("\nPrepare for a game of Rock Paper Scissors Lizard Spock\nYour options are as follows: ", end='')
for i in Options:
    print(f"{i}, ", end='')

print('\n')
for i in Options:
    print(f"{i} will win against: {Options[Pairs[i][0]]} and {Options[Pairs[i][1]]}")



def play():
    Choice = str(input("\nChoose your weapon: "))
    Computer = random.randint(0,4)
    if Choice not in Options:
        print("Invalid input")
        play()
    elif Computer==Options.index(Choice):
        print(f"The computer chose {Options[Computer]}\nDraw!")
        play()
    elif Computer in Pairs[Choice]:
        print(f"The computer chose {Options[Computer]}\nYou won!")
        play()
    else:
        print(f"The computer chose {Options[Computer]}\nYou got beaten by the computer")
        play()

play()
