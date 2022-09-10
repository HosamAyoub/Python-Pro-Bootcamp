from art import logo
from art import vs
from game_data import data
from random import choice

def pick ():
    return choice(data)
    

print(logo)
first_choice = pick()
print(vs)