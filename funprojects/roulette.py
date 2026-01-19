import random
name = input("Welcome to the Casino! The game you will be playing is Poker. Enter Your Name Here: ")

Starting_Stack = 10000
small_blind = 50 
big_blind = 100

ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

rank = random.choice(ranks)
suit = random.choice(suits)

while True:
    if name.isdigit() or name.strip() == "":
        #name.isdigit() checks whether name includes digits
        #name.strip() makes sure that the user didn't type spaces or numbers
        name = input("ERROR! Please Enter a Valid Name: ")
    else:
        print(f"Welcome {name}, you will now be playing Texas Holdem (Poker).")
        break

card1 = f"{rank} of {suit}"
card2 = f"{random.choice(ranks)} of {random.choice(suits)}"
print(f"Your cards are {card1} and {card2}, ")


