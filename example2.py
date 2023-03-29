#!python3

"""
Pro tip!

You can import a module so that it does not need the mdule name with the .
Be careful!  It imports the functions as though they were a part of your program,
so you can't reuse any of the names of functions.
"""

from random import randint
""" Note that we do not need to use random.randint(5,10) to use this
function now!
"""
x = randint(5,10)
print(x)

"""
Since we only importd randint, none of the other commands are available though
"""

x = randrange(4)
x = random.randrange(4)
"""
notice that randrange is not available
also, random is not available because we haven't imported the module

"""