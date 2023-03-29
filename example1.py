#!python3

import random
"""
The random module is imported just like math.  You can use any of the functions
in the module by including 'random.' in front of the function names

visit: https://docs.python.org/3/library/random.html for some of the
possibilities
"""

def rand1(max):
    for i in range(5):
        x = random.randrange(max)
        print(x, end=" ")

def rand2():
    for i in range (20):
        x = random.randint(5,10)
        print(x, end=" ")

def rand3():
    for i in range(20):
        print( random.random(), end = " ")

def rand4():
    myList = ["dog", "cat", "turtle", "fish", "meow", "phone"]
    print(myList)
    for i in range(20):
        random.shuffle(myList)
        print(myList)

if __name__ == "__main__":
    inval = ""
    while inval not in ['1','2','3','4','5']:
        print("\n\n\n")
        print("1. randomrange(5)")
        print("2. randint(5,10)")
        print("3. random.random()")
        print("4. random.shuffle[list]")
        print("5. Exit")
        inval = input("Choose an option:")
    if inval == "1":
        rand1(5)
    elif inval == "2":
        rand2()
    elif inval == "3":
        rand3()
    elif inval == "4":
        rand4()