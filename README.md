## SDSS Computing Studies Python Assignment
### Assignment #7 Random Numbers (Marks 10)

Objectives:
* To make us of additional modules and se what commands are avaiable in them
* To import modules into the current namespace
* To use randomness to generate games of chance
* Explore the randomrange, randint, random and shuffle functions

Randomness is an important part of games, or for a variety of other applications.  Today, we will look at incorporating random numbers into programs.
Random libraries will often contain a "seed".  Early random functions were not really very random, and would actually generate the same sequence of numbers all of the time.  Developers learned to start with a random "seed" which would generate increased randomness.  Often, the seed is based on the current time, but this can be predicted (by setting your clock ahead) and is not generally a good idea.

Consider the generation of a new bitcoin address: \
https://www.bitaddress.org/bitaddress.org-v3.3.0-SHA256-dec17c07685e1870960903d8f58090475b25af946fe95a734f88408cef4aa194.html \
It NEEDS to be random, otherwise it is hackable.  This uses user generated randomness to create the bitcoin address.



Note: There is no autograder for this assignment.
### 4 Tasks, 2 Problems

##### Task 1
Number Guessing Game
Have the computer generate a random number from 1 to 100.  The players will try to guess the number, and the computer will tell them if they are too high or too low.  Play continues until they guess correctly at which point the computer tells them how many guesses it took.
(2 points) 

##### Task 2
Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
(2 points)

##### Task 3
Rock Paper Scissors
Create the classic "Rock, Paper Scissors Game"
(5 points)
Extension:
Play the classic "Rock Paper Scissors Lizard Spock" game
https://www.youtube.com/watch?v=Z2Dwxv-EMTM

##### Task 4
Dungeons and Dragons Character Generator
In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.  The statistics recorded are:
strength
intelligence
wisdom
dexterity
constitution
charisma
Create a character generator that generates a character's statistics
(3 points)

##### Problem 1
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
Add these as options to your D&D Character Statistics Generator

##### Problem 2
Create a list that contains a deck of cards.
Shuffle and deal 5 card hands to 2 different players.  You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.



