#! python3

import random

stats = [{'Strength': [0]}, {'Dexterity': [1]}, {'Constitution': [2]}, {'Intelligence': [3]}, {'Wisdom': [4]}, {'Charisma': [5]}]

def Input():
    Choice = input("Choose option a, b, or c:\na) roll 3 dice\nb) roll 4 dice, discard the lowest\nc) roll 3 dice, reroll 1s\n")
    if Choice=='a':
        A()
    elif Choice=='b':
        B()
    elif Choice=='c':
        C()
    else:
        print("Invalid input")
        Input()

def A():
    for i in stats:
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        n = str(stats[stats.index(i)].keys())-"dict_keys([''])"
        print(n)




print("D&D character stat generator")
Input()
