#! python3


import random
n = random.randint(1,100)
x = -1
t = 0
while x!=n:
    x = int(input("Enter a number between and including 1 and 100: "))
    t = t+1
    if x<n:
        print("Your guess was too low")
    elif x>n:
        print("Your guess was too high")
print(f"Your guess was correct!\nyou took {t} tries to guess the correct number")