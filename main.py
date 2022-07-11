import random
from art import logo
from replit import clear

def cal_sum(TheCards, role):
  """calculates and prints the current score of the user or the first score of the dealer."""
  Summ = 0
  for i in range(len(TheCards)):
    Summ += TheCards[i]
  if 11 in TheCards and Summ > 21:
    Summ = Summ - 10
  #global score
  #score = Summ #delete if not used
  if role == "user":
    global user_score
    user_score = Summ
    return print(f"\nYour cards: {TheCards}, Current Score: {user_score}")
  elif role == "Dealer":
    global dealer_score
    dealer_score = Summ
    if len(TheCards) == 2:
      return print(f"The dealer's first card: {DealersCards[0]}")

def a_BlackJack(TheCards, role, score):
  """ Checks if the user or the dealer has a Black Jack. """
  if len(TheCards) == 2 and score == 21:     #if the dealer and the user get a 21, then there is a push.
    if role == "user":
      print("          Congratulations, you have a 'BlackJack'")
    elif role == "Dealer":
      print("          Opps, the dealer has a 'BlackJack'")
    return True
    

def a_bust(TheCards, role, score):
  """ Checks if the user or the dealer busts. At which stage there would be no need to compare hands."""
  if score > 21:     #A bust.... Game ends
    print(f"     That's a 'bust'. The {role}'s score exceeds 21.")
    return "y"


def deal_card_to(TheCards, role):
  """deals cards when the user or the dealer decides to hit. Result: Prints out the user's hand and his current score."""
  TheCards.append(random.sample(cards, 1)[0])
  cal_sum(TheCards, role)


def compare(user_score, dealer_score):
  """ compares both scores to check whose score is higher. """
  if user_score > dealer_score and dealer_score <= 21:
    print("\nCongratulations!!! You win 🎉🎉🎉")
  elif user_score < dealer_score and dealer_score <= 21:
    print("\nYou lose 😔 and the Dealer wins")
  elif user_score == dealer_score and dealer_score <= 21:
    print("\nIt's a 'Push' 😐.... Try again")

new_game = "y"

new_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
while new_game == "y":
  clear()
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  should_game_end = False
  usersCards = random.sample(cards, 2)
  DealersCards = random.sample(cards, 2)
  
  cal_sum(usersCards, "user")
  cal_sum(DealersCards, "Dealer")

  userBlackJack = a_BlackJack(usersCards, "user", user_score)
  dealerBlackJack = a_BlackJack(usersCards, "Dealer", dealer_score)

  if userBlackJack == True and dealerBlackJack == True:
    print("          You both have BlackJacks. It's a 'Push'.... Try again")
  elif userBlackJack == True and dealerBlackJack == False:
    print("          You win 🎉🎉🎉")
  elif userBlackJack == False and dealerBlackJack == True:
    print("          You lose 😔 and the Dealer wins")
  
  if userBlackJack == True or dealerBlackJack == True:
    continue
  
  
  next_move = "h"
  while next_move == "h":
    next_move = input("Type 'h' to get another card (hit), type 's' to pass (Stand). ")
    if next_move == "h":
      deal_card_to(usersCards, "user")
      should_game_end = a_bust(usersCards, "user", user_score)
      if should_game_end == "y":
        print("          You lose 😔 ")
        break
    elif next_move == "s":
      while dealer_score < 17:
        deal_card_to(DealersCards, "Dealer")
        should_game_end = a_bust(DealersCards, "Dealer", dealer_score)
        if should_game_end == "y":
          print("    You win 🎉🎉🎉")
          break
        #Compare the scores
      print(f"\nYour final hand: {usersCards}. Your score: {user_score}.\nDealer's final hand: {DealersCards}, Dealer score: {dealer_score}.")
      compare(user_score, dealer_score)
    else:
      print("type in the right syntax")
    
  new_game = input("\n-------------------------------\nDo you want to play another game of Black Jack? Type 'y' or 'n': ")

print("Until next time, goodbye.")
