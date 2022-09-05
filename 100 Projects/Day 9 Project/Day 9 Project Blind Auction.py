from replit import clear
from art import logo
auction = {}

def find_highest_bidder(bidding_dict):
    maximum = 0
    winner = ""
    for key in bidding_dict:
        if bidding_dict[key] > maximum:
            maximum = auction[key]
            winner = key
    
    print(f"The winner is {winner} with a bid of ${maximum}")


def record_bidding(bidding_dict):
    while (True):
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n$"))
        bidding_dict[name] = bid
        continue_state = input("Are there any other bidders?\nType anything to continue or 'no' to stop.\n")
        if (continue_state == "no" or continue_state == "No" or continue_state == "NO"             or continue_state == "nO"):
            break
        clear()


def blind_auction (bidding_dict):
    record_bidding(bidding_dict)
    find_highest_bidder(bidding_dict)

print(logo)
blind_auction(auction)