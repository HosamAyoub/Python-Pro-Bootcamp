from art import logo
from art import vs
from game_data import data
from random import choice

def pick ():
    return choice(data)
    

print(logo)
first_choice = pick()
print(f"Compare A: {first_choice["name"]}, a {first_choice["description"]}, from {first_choice['country']}.")
print(vs)