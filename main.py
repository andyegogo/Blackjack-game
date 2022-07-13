import random
from art import logo
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def cal_sum(the_cards, role):
    """calculates and prints the current score of the user or the first score of the dealer."""
    sum_ = 0
    for i in range(len(the_cards)):
        sum_ += the_cards[i]
    if 11 in the_cards and sum_ > 21:
        sum_ -= 10
    if role == "user":
        # global user_score_
        user_score_local = sum_
        print(f"\nYour cards: {the_cards}, Current Score: {user_score_local}")
        return user_score_local
    elif role == "Dealer":
        # global dealer_score_
        dealer_score_local = sum_
        if len(the_cards) == 2:
            print(f"The dealer's first card: {dealer_cards[0]}")
        return dealer_score_local


def a_blackjack(the_cards, role, score):
    """ Checks if the user or the dealer has a Black Jack. """
    if len(the_cards) == 2 and score == 21:  # if the dealer and the user get a 21, then there is a push.
        if role == "user":
            print("          Congratulations, you have a 'BlackJack'")
        elif role == "Dealer":
            print("          Opps, the dealer has a 'BlackJack'")
        return True


def a_bust(role, score):
    """ Checks if the user or the dealer busts. At which stage there would be no need to compare hands."""
    if score > 21:  # A bust.... Game ends
        print(f"     That's a 'bust'. The {role}'s score exceeds 21.")
        return "y"


def deal_card_to(the_cards, role):
    """deals cards when the user or the dealer decides to hit. Result: Prints out the user's hand and his current score."""
    the_cards.append(random.choice(cards))
    return cal_sum(the_cards, role)


def compare(user_score_, dealer_score_):
    """ compares both scores to check whose score is higher. """
    global user_cash
    if user_score_ > dealer_score_ and dealer_score_ <= 21:
        print("\nCongratulations!!! You win 🎉🎉🎉")
        user_cash = user_cash + user_bet
    elif user_score_ < dealer_score_ <= 21:
        print("\nYou lose 😔 and the Dealer wins")
        user_cash = user_cash - user_bet
    elif user_score_ == dealer_score_ and dealer_score_ <= 21:
        print("\nIt's a 'Push' 😐.... Try again")


user_cash = 0
new_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
while new_game == "y":
    clear_screen()
    print(logo)
    user_bet = input("Place a bet, 'a' for $50 or 'b' for $100. ")
    if user_bet == "a":
        user_bet = 50
    elif user_bet == "b":
        user_bet = 100
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    should_game_end = False
    user_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)

    user_score = cal_sum(user_cards, "user")
    dealer_score = cal_sum(dealer_cards, "Dealer")

    user_has_blackjack = a_blackjack(user_cards, "user", user_score)
    dealer_has_blackjack = a_blackjack(user_cards, "Dealer", dealer_score)

    if user_has_blackjack is True or dealer_has_blackjack is True:
        if user_has_blackjack is True and dealer_has_blackjack is True:
            print("          You both have BlackJacks. It's a 'Push'.... Try again")
        elif user_has_blackjack is True and dealer_has_blackjack is False:
            print("          You win 🎉🎉🎉")
            user_cash = user_cash + user_bet
        elif user_has_blackjack is False and dealer_has_blackjack is True:
            print("          You lose 😔 and the Dealer wins")
            user_cash = user_cash - user_bet
        new_game = input(
            "\n-------------------------------\nDo you want to play another game of Black Jack? Type 'y' or 'n': ")
        continue

    next_move = "h"
    while next_move == "h":
        next_move = input("Type 'h' to get another card (hit), type 's' to pass (Stand). ")
        if next_move == "h":
            user_score = deal_card_to(user_cards, "user")
            should_game_end = a_bust("user", user_score)
            if should_game_end == "y":
                print("          You lose 😔 ")
                user_cash = user_cash - user_bet
                break
        elif next_move == "s":
            # The dealer's turn
            while dealer_score < 17:
                dealer_score = deal_card_to(dealer_cards, "Dealer")
                should_game_end = a_bust("Dealer", dealer_score)
                if should_game_end == "y":
                    print("    You win 🎉🎉🎉")
                    user_cash = user_cash + user_bet
                    break
            # Compare the scores
            print(
                f"\nYour final hand: {user_cards}. Your score: {user_score}.\nDealer's final hand: {dealer_cards}, Dealer score: {dealer_score}.")
            compare(user_score, dealer_score)
        else:
            print("type in the right syntax")

    new_game = input(
        "\n-------------------------------\nDo you want to play another game of Black Jack? Type 'y' or 'n': ")

# print(Your total wins)
if user_cash < 0:
    print(f"Your owe a total of ${abs(user_cash)}")
elif user_cash > 0:
    print(f"You've made a total of ${abs(user_cash)}")
else:
    print("You have $0")
print("Until next time, goodbye.")
