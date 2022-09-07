############### Blackjack Project #####################
from art import logo
from random import choice
from replit import clear


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards_list):
    """Returns the total score of the list.
    Takes care of the corner cases."""
    if (sum(cards_list) == 21) and (len(cards_list) == 2):
        return 0
    elif (sum(cards_list) > 21) and (11 in cards_list):
        cards_list.remove(11)
        cards_list.append(1)
        return sum(cards_list)
    else:
        return sum(cards_list)


def compare(player_total_score, computer_total_score):
    """Returns the winner."""
    if (player_total_score == 0) and (computer_total_score == 0):
        return "Draw, both of you got a Blackjack 🤯"
    elif (computer_total_score == 0):
        return "Lose, opponent has Blackjack 😱"
    elif (player_total_score == 0):
        return "Win, with a Blackjack 😎"
    elif (player_total_score > 21):
        return "You went over. You lose 😭"
    elif (computer_total_score > 21):
        return "Opponent went over. You win 😁"
    elif (computer_total_score == player_total_score):
        return "Draw 🙃"
    elif (player_total_score > computer_total_score):
        return "You win 😃"
    else:
        return "You lose 😤"


def show_score(player_final_score, player_final_cards, computer_final_score,
               computer_final_cards):
    """Prints the player and computer final score and cards"""
    if player_final_score == 0:
        player_final_score = 21
    if computer_final_score == 0:
        computer_final_score = 21
    print(
        f"Your cards: {player_final_cards}, final score: {player_final_score}")
    print(
        f"Computer's final hand: {computer_final_cards}, final score: {computer_final_score}"
    )


def black_jack():
    """The logic of the black jack game"""
    while (True):
        if (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                == 'n'):
            print("Goodbye!")
            break
        player = []
        computer = []
        clear()
        print(logo)
        for i in range(2):
            player.append(deal_card())
            computer.append(deal_card())
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        if (player_score == 0):
            print(f"Your cards {player}, current score: {player_score + 21}")
            print(f"Computer's first card: {computer[0]}")
            while (computer_score < 16) and (computer_score != 0):
                computer.append(deal_card())
                computer_score = calculate_score(computer)
        else:
            print(f"Your cards {player}, current score: {player_score}")
            print(f"Computer's first card: {computer[0]}")
            while (input("Type 'y' to get another card, type 'n' to pass: ") ==
                   'y'):
                player.append(deal_card())
                player_score = calculate_score(player)
                print(f"Your cards {player}, current score: {player_score}")
                print(f"Computer's first card: {computer[0]}")
            while (computer_score < 16) and (computer_score != 0):
                computer.append(deal_card())
                computer_score = calculate_score(computer)
        result = compare(player_score, computer_score)
        show_score(player_score, player, computer_score, computer)
        print(result)


black_jack()
