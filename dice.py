import random

def roll():
    die1 = random.randrange( 1, 7 )
    die2 = random.randrange( 1, 7 )
    return [die1, die2]
