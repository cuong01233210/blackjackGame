

from art import logo
import random








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




