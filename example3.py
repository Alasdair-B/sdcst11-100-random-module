#!python3
""" This is a program to simulate the toss of 2 dice.
A winning roll is if the computer rolls higher than the player.
Note, this actually, just simulates the game mechanics.
"""

import random

def playerRolls():
    # input: none
    # generates 2 random numbers from 1 to 6
    # return list [integer, integer]
    a = random.randint(1,6)
    b = random.randint(1,6)
    return [a,b]

def main():
        # generate the roll for player
        inVal = ""
        while inVal.upper != "X":
            player = playerRolls()
            print(f"You rolled {player[0] + player[1]}")
            # the computer has a 50% chance to win
            computerWin = random.randint(1,2)
            if computerWin == 1:
                print(f"aww. The computer rolled {player[0] + player[1] +1}...You lost")
            else:
                print(f"Whee!. The computer rolled {player[0] + player[1] - 1}...You win!")
            inVal = input("Press Enter to play again! Press x to quit")

if __name__ == "__main__":
    main()