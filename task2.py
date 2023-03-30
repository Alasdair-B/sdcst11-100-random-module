#! python3

import random
import time

n = random.randint(1,2)
g = int(input("Type 1 to pick Heads, type 2 to pick Tails: "))
time.sleep(0.5)
print("[flipping coin]")
time.sleep(1.3)

if n==1:
    print("The coin landed on Heads")
elif n==2:
    print("The coin landed on Tails")

if g==n:
    print("Your guess was correct!")
else:
    print("Your guess was incorrect")
