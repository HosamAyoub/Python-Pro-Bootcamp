from art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_guess(user_guess, random_number, turns):
    """Check if the answer was right or wrong and if it's wrong it will tell him if his guess was too high or too low then return the remaining attempts"""
    if (user_guess < random_number):
        print("Too low.")
        if (turns > 1):
            print("Try again.")
        else:
            print("You've run out of guesses, you lose.")
        return turns - 1
    elif (user_guess > random_number):
        print("Too high.")
        if (turns > 1):
            print("Try again.")
        else:
            print("You've run out of guesses, you lose.")
        return turns - 1
    else:
        print(f"You got it! The answer was {random_number}.")
        return 0
 
def game():
    print(logo)
    rand_num = randint(1, 100)
    print(rand_num)
    print("I'm thinking of a number between 1 and 100.")
    attempts = 0
    while (attempts == 0):
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if (level == "easy") or (level == "Easy") or (level == "EASY"):
            attempts = EASY_ATTEMPTS
        elif (level == "hard") or (level == "HARD") or (level == "HARD"):
            attempts = HARD_ATTEMPTS
        else:
            print("Invalid diffculty! please enter a vaild diffculty.")
    while(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        attempts = check_guess(guess, rand_num, attempts)

game()