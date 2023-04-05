#! python3

import random
import math

stats = [{'name':'Strength', 'Val': [0]}, {'name':'Dexterity', 'Val': [1]}, {'name':'Constitution', 'Val': [2]}, {'name':'Intelligence', 'Val': [3]}, {'name':'Wisdom', 'Val': [4]}, {'name':'Charisma', 'Val': [5]}]

def Input():
    Choice = input("\nChoose option a, b, or c:\na) roll 3 dice\nb) roll 4 dice, discard the lowest\nc) roll 3 dice, reroll 1s\nd) both b and c\n")
    if Choice=='a':
        A()
    elif Choice=='b':
        B()
    elif Choice=='c':
        C()
    elif Choice=='d':
        D()
    else:
        print("Invalid input")
        Input()

def reroll():
    z = 0
    while 1>=z:
        z = random.randint(1,6)
    return z

def A():
    for i in stats:
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        n = str(stats[stats.index(i)]['name'])
        print(f"{n} is {a+b+c} ({math.floor(((a+b+c)-10)/2.0)})")
    Input()

def B():
    for i in stats:
        l = sorted([random.randint(1,6) for x in range(0,4)])
        v = sum(l)-l[0]
        n = str(stats[stats.index(i)]['name'])
        print(f"{n} is {v} ({math.floor(((v)-10)/2.0)})")
    Input()

def C():
    for i in stats:
        l = [reroll() for x in range(0,3)]
        n = str(stats[stats.index(i)]['name'])
        print(f"{n} is {sum(l)} ({math.floor(((sum(l))-10)/2.0)})")
    Input()

def D():
    for i in stats:
        l = sorted([reroll() for x in range(0,4)])
        v = sum(l)-l[0]
        n = str(stats[stats.index(i)]['name'])
        print(f"{n} is {v} ({math.floor(((v)-10)/2.0)})")
    Input()


print("D&D character stat generator")
Input()
