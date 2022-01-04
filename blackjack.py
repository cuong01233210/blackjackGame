

from art import logo
import random



############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cardborn():
  ran_card_pos = random.randint(0, len(cards) - 1)
  return cards[ran_card_pos]


  

def blackjack():
  my_deck = []
  com_deck = []
  
  my_deck.append(cardborn())
  my_deck.append(cardborn())
  com_deck.append(cardborn())
  com_deck.append(cardborn())
  my_point = my_deck[0] + my_deck[1]
  if my_point == 22:
    my_point = 12
    my_deck[1] = 1
  com_point = com_deck[0] + com_deck[1]
  if com_point == 22:
    com_point = 12
    com_deck[1] = 1
  
  print(f"cards in my hand {my_deck}, current points: {my_point} ")
  print(f"computer's first cards {com_deck[0]}")

  want_to_get_another = input("Type 'y' to get another card, type 'n' if you don't want this ")
  while want_to_get_another == "y":
    my_deck.append(cardborn())
    my_point = sum(my_deck)
    if my_point > 21 and "11" in my_deck:
      for i in range(0, len(my_deck)):
        if my_deck[i] == 11:
          print("Your points are beyond 21 and you have ace, so I change your ace to 1")
          my_deck[i] = 1
          break
    elif my_point > 21 and "11" not in my_deck:
      print(my_deck)
      print(f"Your point is {sum(my_deck)}, is beyond 21, so you lose")
      return 
    my_point = sum(my_deck)
    print(f"cards in my hand {my_deck}, current points: {my_point} ")
    want_to_get_another = input("Type 'y' to get another card, type 'n' if you don't want this ")
  while sum(com_deck) < 16:
    com_deck.append(cardborn())
    com_point = sum(com_deck)
    if com_point > 21 and "11" in com_deck:
      for i in range(0, len(com_deck)):
        if com_deck[i] == 11:          
          com_deck[i] = 1
          break
  if my_point < 16:
    print("game over, you loss")
    return
  
  print(f"cards the com has {com_deck}")
  print(f"computer's points: {sum(com_deck)}")
  if (sum(com_deck) < sum(my_deck)) or sum(com_deck) >21:
    print("You win")
  else:
    print("You loss")

  
    











start = 1
def khoitao():
  play_game = input("Do you want to have a game of Blackjack 'y' / 'n' ")
  if play_game == 'y':
    
    print(logo)
    return 1
  else: 
    return 0
  
    
  
start = khoitao()
while start == 1:
  blackjack()
  
  start = khoitao()




