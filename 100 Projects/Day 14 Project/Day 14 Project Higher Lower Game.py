from art import logo
from art import vs
from game_data import data
from random import choice

def pick ():
    return choice(data)
    

print(logo)
first_choice = pick()
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
print(vs)
second_choice = first_choice
while(second_choice == first_choice):
    second_choice = pick()
print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")