from art import logo, vs
from game_data import data
from random import choice
from replit import clear

def pick ():
    return choice(data)

def solution(choice):
    choice = ""
    while (choice.upper() != 'A') and (choice.upper() != 'B'):
        choice = input("Who has more followers? Type 'A' or 'B': ")
    if (first_choice["follower_count"] > second_choice["follower_count"]):
        right_choice = 'A'
    elif (first_choice["follower_count"] < second_choice["follower_count"]):
        right_choice = 'B'
    else:
        right_choice = 'Both'
    return right_choice

score = 0
print(logo)
first_choice = pick()
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
print(vs)
second_choice = first_choice

while(second_choice == first_choice):
    second_choice = pick()

print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")

answer = ""
while (answer.upper() != 'A') and (answer.upper() != 'B'):
    answer = input("Who has more followers? Type 'A' or 'B': ")

right_answer  = solution(answer)
while ((answer.upper() == right_answer) or (right_answer == 'Both')):
    clear()
    score += 1
    print(f"You're right! Current score: {score}")
    first_choice = second_choice
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(vs)
    
    while(second_choice == first_choice):
        second_choice = pick()

    print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    right_answer  = solution(answer)

print(f"Sorry, that's wrong. Final score: {score}")