import random
from time import sleep
from logo import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
hidden_card = []

# Randomly select the value of Cards for human and computer
for deal in range(0, 2):
    deal_cards = random.choice(cards)
    user_cards.append(deal_cards)
    deal_cards = random.choice(cards)
    computer_cards.append(deal_cards)

# add the first value hidden_card to anonymize the first value of computer cards(see line 86)
hidden_card = computer_cards[0]


def user_play():
    """Creating a computer_play function"""
    print("..........................HUMAN PLAYING..........................")
    sleep(3)
    stop = False

    while not stop:
        sum_user_cards = sum(user_cards)
        print(f"Your cards are: {user_cards}")
        if sum_user_cards < 21:
            add_card = input("\nDo you want to add 1 more card? Type 'Yes' or 'No': ").lower()
            if add_card == 'yes':
                random.choice(cards)
                user_cards.append(random.choice(cards))
            else:
                stop = True
        if sum_user_cards == 21:
            stop = True
        elif 11 in user_cards:
            if sum_user_cards >= 22:
                user_cards.remove(11)
                user_cards.append(1)
                stop = True
        elif sum_user_cards >= 22:
            stop = True


def computer_play():
    """Creating a computer_play function"""
    print("\n\n.........................COMPUTER PLAYING........................")
    sleep(3)
    stop = False

    while not stop:
        sum_computer_cards = sum(computer_cards)
        if sum_computer_cards < 15:
            random.choice(cards)
            computer_cards.append(random.choice(cards))
        else:
            stop = True

        if sum_computer_cards == 21:
            stop = True
        elif 11 in computer_cards:
            if sum_computer_cards >= 22:
                computer_cards.remove(11)
                computer_cards.append(1)
                stop = True
        elif sum_computer_cards >= 22:
            stop = True


def reset_game():
    # resetting the value on the list
    global user_cards, computer_cards, hidden_card
    user_cards = []
    computer_cards = []
    hidden_card = []
    # Randomly select the value of Cards for human and computer
    for new in range(0, 2):
        new_cards = random.choice(cards)
        user_cards.append(new_cards)
        new_cards = random.choice(cards)
        computer_cards.append(new_cards)
    hidden_card = computer_cards[0]


def calculate_score(sum_user_cards=sum(user_cards), sum_computer_cards=sum(computer_cards)):
    """ Determining the winner by calling calculate_score """

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    computer_play()
    # Calling the computer_play function and set condition to determine the next action
    sum_computer_cards = sum(computer_cards)
    if sum_computer_cards >= 22:
        sum_computer_cards -= 21
    elif sum_computer_cards == 21:
        print("Computer have BLACKJACK Cards.")

    # Saving the first value to hidden_card = computer_cards[0]. To replace the first value of list.
    computer_cards[0] = "?"
    print(f"Computer's First Card Is Hidden: {computer_cards}\n")

    user_play()
    # Calling the user_play function and set condition to determine the next action
    sum_user_cards = sum(user_cards)
    if sum_user_cards >= 22:
        sum_user_cards -= 21
        print(f"\nYour total card is {sum_user_cards}.\n")
    elif sum_user_cards == 21:
        print("You have BLACKJACK Cards.\n")
    else:
        print(f"\nYour total card is {sum_user_cards}.\n")

    # Revealing the computer's hidden card
    print("Revealing Computer's Card.")
    sleep(3)
    print(f"The Computer's hidden Card is {hidden_card}.")
    computer_cards[0] = hidden_card
    print(f"The Computer's Cards are {computer_cards}.")
    print(f"The Computer's total card is {sum_computer_cards}.\n")

    # Comparing the cards to determine the winner
    if sum_user_cards < sum_computer_cards:
        print("Computer Player Win.")
    elif sum_user_cards > sum_computer_cards:
        print("Human Player Win.")
    else:
        print("It is a Draw Game.")
    sleep(10)
    reset_game()
    calculate_score(sum_user_cards=sum(user_cards), sum_computer_cards=sum(computer_cards))
    # Recursion


calculate_score(sum_user_cards=sum(user_cards), sum_computer_cards=sum(computer_cards))
# Calling the calculate_score function


sleep(10)
