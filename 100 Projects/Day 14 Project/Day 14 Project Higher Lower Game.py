from art import logo
from art import vs
from game_data import data
from random import choice

def pick ():
    return choice(data)
    

answer = None
score = 0
print(logo)
first_choice = pick()
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
print(vs)
second_choice = first_choice
while(second_choice == first_choice):
    second_choice = pick()
print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")

while ((answer != 'A') and (answer != 'B')) or ((answer != 'a') and (answer != 'b')):
    answer = input("Who has more followers? Type 'A' or 'B': ")
if (first_choice["follower_count"] > second_choice["follower_count"]):
    right_answer = 'A'
elif (first_choice["follower_count"] < second_choice["follower_count"]):
    right_answer = 'B'
else:
    right_answer = 'Both'
while ((answer == right_answer) or (right_answer == 'Both')):
    score += 1
    print(f"You're right! Current score: {score}")
    first_choice = second_choice
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(vs)
    second_choice = first_choice
    while(second_choice == first_choice):
        second_choice = pick()
    print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    while ((answer != 'A') and (answer != 'B')) or ((answer != 'a') and (answer != 'b')):
        answer = input("Who has more followers? Type 'A' or 'B': ")
    if (first_choice["follower_count"] > second_choice["follower_count"]):
        right_answer = 'A'
    elif (first_choice["follower_count"] < second_choice["follower_count"]):
        right_answer = 'B'
    else:
        right_answer = 'Both'
else:
    print(f"Sorry, that's wrong. Final score: {score}")