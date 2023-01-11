from art import logo

join_player = True
players_bid = {}

def find_highest_bid():
    highest_player = max(players_bid, key=players_bid.get)
    print(f"The winner is {highest_player} with bid of ${players_bid[highest_player]}")
        

print(logo)

while join_player:
    name = input("What is your name? ")
    bid = input("What's your bid? $")

    players_bid[name] = bid

    have_other_player = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if have_other_player == "yes":
        print("clear")
    else:
        join_player = False
        find_highest_bid()
