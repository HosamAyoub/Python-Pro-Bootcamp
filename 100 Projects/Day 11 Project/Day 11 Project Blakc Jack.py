############### Blackjack Project #####################
from art import logo
from random import choice
from replit import clear

def calculator(cards_list):
    if (sum(cards_list) == 21) and (len(cards_list) == 2):
        return 0
    elif (sum(cards_list) > 21) and (11 in cards_list):
        cards_list.remove(11)
        cards_list.append(1)
        return sum(cards_list)
    else:
        return sum(cards_list)
        

def compare(player_total_score, computer_total_score):
    if (player_total_score == 0) and (computer_total_score == 0):
        print("Draw, both of you got a Blackjack 🤨")
    elif (computer_total_score == 0):
        print("Lose, opponent has Blackjack 😱")
    elif (player_total_score == 0):
        print("Win, with a Blackjack 😎")
    elif (player_total_score > 21):
        print("You went over. You lose 😭")
    elif (computer_total_score > 21):
        print("Opponent went over. You win 😁")
    elif (computer_total_score == player_total_score):
        print("Draw 🙃")
    elif (player_total_score > computer_total_score):
        print("You win 😃")
    else:
        print("You lose 😤")

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    computer = []
    while(True):
        if (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n'):
            print("Goodbye!")
            break
        player.clear()
        computer.clear()
        clear()
        print(logo)
        player.append(choice(cards))
        player.append(choice(cards))
        computer.append(choice(cards))
        computer.append(choice(cards))
        player_score = calculator(player)
        computer_score = calculator(computer)
        print(f"Your cards {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")
        if (player_score == 0) and (computer_score == 0):
            print(f"Your cards: {player}, final score: {player_score + 21}")
            print(f"Computer's final hand: {computer}, final score: {computer_score + 21}")
            compare(player_score, computer_score)
        elif (player_score == 0):
            while (computer_score < 16):
                computer.append(choice(cards))
                computer_score = calculator(computer)
            print(f"Your cards: {player}, final score: {player_score + 21}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            compare(player_score, computer_score)
        elif (computer_score == 0):
            print(f"Your cards: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score + 21}")
            compare(player_score, computer_score)
        else:
            while (input("Type 'y' to get another card, type 'n' to pass: ") == 'y'):
                player.append(choice(cards))
                player_score = calculator(player)
                print(f"Your cards {player}, current score: {player_score}")
                print(f"Computer's first card: {computer[0]}")
            while (computer_score < 16):
                computer.append(choice(cards))
                computer_score = calculator(computer)
            print(f"Your cards: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            compare(player_score, computer_score)

black_jack()