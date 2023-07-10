# Only issue left with ACE and refreshing screen
import random
from art import logo

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def opening_desk():
  """Returns a random card from the deck."""
  cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
  return random.sample(cards,2)


def adding_card(deck):
  return deck.append(random.choice(cards))


def replace_cards(cards_list):
    """Replaces 'J', 'Q', and 'K' with 10 in the given list."""
    for i in range(len(cards_list)):
        if cards_list[i] == "J" or cards_list[i] == "Q" or cards_list[i] == "K":
            cards_list[i] = 10
        if cards_list[i] == "Ace":
            cards_list[i] = 11  


def value_of_deck(deck):
   value = 0
   replace_cards(deck)
   for element in deck:
     value += int(element)  
   return value

    
computer_deck = [] 
user_deck = []

is_game_ended = False
def main():
  print(logo)
  global is_game_ended
  computer_deck.extend(opening_desk())
  user_deck.extend(opening_desk())
  print(f"Your cards: {user_deck} Current score: {value_of_deck(user_deck)} ")
  firstcard_computer = [computer_deck[0]]
  print(f"Computers first card: {firstcard_computer}")
  while is_game_ended == False:
    answer = input("Type 'y' to get another card, type 'n to pass': ").lower()
    if answer == 'y':
      adding_card(user_deck)
      print(f"Current score: {value_of_deck(user_deck)}")
      if value_of_deck(user_deck) > 21:
        print("You went over you lose")
        is_game_ended = True
      
    if answer == 'n':
      while value_of_deck(computer_deck) <= 16:
        adding_card(computer_deck)
 
      if value_of_deck(computer_deck) > 21:
        print(f"Computure's final hand is {computer_deck}, Score is {value_of_deck(computer_deck)}")
        print(f"Your final hand is {user_deck}, Score is {value_of_deck(user_deck)}")
        
        print("Computer went over, you won")
        is_game_ended = True
      elif value_of_deck(computer_deck) > value_of_deck(user_deck):
        print(f"Computure's final hand is {computer_deck}, Score is {value_of_deck(computer_deck)}")
        print(f"Your final hand is {user_deck}, Score is {value_of_deck(user_deck)}")
      
        print("Computer won!")
        is_game_ended = True
      elif value_of_deck(computer_deck) < value_of_deck(user_deck):
        print(f"Computure's final hand is {computer_deck}, Score is {value_of_deck(computer_deck)}")
        print(f"Your final hand is {user_deck}, Score is {value_of_deck(user_deck)}")
        
        print("You have won!")
        is_game_ended = True
      elif value_of_deck(computer_deck) == value_of_deck(user_deck):
        print(f"Computure's final hand is {computer_deck}, Score is {value_of_deck(computer_deck)}")
        print(f"Your final hand is {user_deck}, Score is {value_of_deck(user_deck)}")
        
        print("Draw!")
        is_game_ended = True
  another_game = input("Do you wanna play another game; if yes say 'y',  if no say 'n' ").lower()

  if another_game == 'y':
    is_game_ended = False
    computer_deck.clear()
    user_deck.clear()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    main()
    
  if another_game == 'n':
    print("Thanks for playing!")
    
main()  


  
