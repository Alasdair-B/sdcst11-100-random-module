#!python3

import math
import keyboard
import time
import random

ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Clubs','Diamonds','Hearts','Spades']
Deck = []
Pulled1 = []
Pulled2 = []

def deck():
    for s in suits:
        vals = None
        vals = int(suits.index(s))
        for r in ranks:
            valr = None
            valr = int(ranks.index(r))
            Deck.append({'value': int((100*vals)+valr), 'name': str(f"{r} of {s}")})
        
def draw(n):
    p = str(input("Player 1 or 2? "))
    if p=='1':
        print("You drew:")
        if len(Deck)==0:
            print("No cards remain in deck")
            Interface()
        elif n >= len(Deck):
            n = len(Deck)

        for i in range(n):
            print(Deck[0]['name'])
            Pulled1.append(Deck.pop(0))
        
        Interface()
    elif p=='2':
        print("You drew:")
        if len(Deck)==0:
            print("No cards remain in deck")
            Interface()
        elif n >= len(Deck):
            n = len(Deck)

        for i in range(n):
            print(Deck[0]['name'])
            Pulled2.append(Deck.pop(0))
        
        Interface()
    else:
        Interface()

def shuffle():
    random.shuffle(Deck)
    print("The deck has been shuffled\n")
    Interface()

def sort():
    Deck.sort(key= lambda x: x['value'])
    print("The deck has been sorted\n")
    Interface()

def disDeck():
    print("The cards currently still in the deck are:")
    for i in range(len(Deck)):
        print(Deck[i]['name'])

    Interface()

def disHand():
    p = str(input("Player 1 or 2? "))
    if p=='1':
        print("The cards currently in your hand are:")
        for i in range(len(Pulled1)):
            print(Pulled1[i]['name'])
        Interface()
    elif p=='2':
        print("The cards currently in your hand are:")
        for i in range(len(Pulled2)):
            print(Pulled2[i]['name'])
        Interface()
    else:
        Interface()

def Return():
    p = str(input("Player 1 or 2? "))
    if p=='1':
        for i in range(len(Pulled1)):
            Deck.append(Pulled1.pop(i))
        print("Your hand has been returned to the deck\n")
        Interface()
    elif p=='2':
        for i in range(len(Pulled2)):
            Deck.append(Pulled2.pop(i))
        print("Your hand has been returned to the deck\n")
        Interface()
    else:
        Interface()

def Interface():
    time.sleep(1)
    print("\nto see your hand, press h")
    print("to draw a card, press d")
    print("to return your hand to the deck, press r")
    print("to shuffle the deck, press s")
    print("to sort the deck by rank and suit, press o")
    print("to view all cards currently in the deck, press v\n")
    while True:
        if keyboard.is_pressed("h"):
            disHand()

        elif keyboard.is_pressed("d"):
            N = int(input("enter the number of cards you wish you draw:\n"))
            if (0 >= N) or (math.floor(N) != N):
                print("Invalid input")
                Interface()
            else:
                draw(N)
        
        elif keyboard.is_pressed("r"):
            Return()

        elif keyboard.is_pressed("s"):
            shuffle()

        elif keyboard.is_pressed("o"):
            sort()

        elif keyboard.is_pressed("v"):
            disDeck()
            


print("\nThis is an interactive simulation of a deck of cards\nKeyboard module must be installed to run")
deck()
Interface()
