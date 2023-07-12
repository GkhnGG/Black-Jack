import random
from art import logo

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def opening_deck():
    """Returns a random card from the deck."""
    return random.choices(cards, k=2)


def adding_card(deck):
    deck.append(random.choice(cards))


def replace_cards(cards_list):
    """Replaces 'J', 'Q', and 'K' with 10 in the given list."""
    for i in range(len(cards_list)):
        if cards_list[i] == "J" or cards_list[i] == "Q" or cards_list[i] == "K":
            cards_list[i] = 10


def value_of_deck(deck):
    value = 0
    replace_cards(deck)
    ace_count = deck.count("Ace")
    for element in deck:
        if element == "Ace":
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        else:
            value += int(element)
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value


computer_deck = []
user_deck = []

is_game_ended = False


def main():
    print(logo)
    global is_game_ended
    computer_deck.extend(opening_deck())
    user_deck.extend(opening_deck())
    print(f"Your cards: {user_deck} Current score: {value_of_deck(user_deck)}")
    firstcard_computer = [computer_deck[0]]
    print(f"Computer's first card: {firstcard_computer}")

    while not is_game_ended:
        answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if answer == 'y':
            adding_card(user_deck)
            print(f"Your cards: {user_deck} Current score: {value_of_deck(user_deck)}")
            if value_of_deck(user_deck) > 21:
                print("You went over, you lose")
                is_game_ended = True
        elif answer == 'n':
            while value_of_deck(computer_deck) <= 16:
                adding_card(computer_deck)

            print(f"Computer's final hand: {computer_deck}, Score: {value_of_deck(computer_deck)}")
            print(f"Your final hand: {user_deck}, Score: {value_of_deck(user_deck)}")

            if value_of_deck(computer_deck) > 21:
                print("Computer went over, you won!")
            elif value_of_deck(computer_deck) > value_of_deck(user_deck):
                print("Computer won!")
            elif value_of_deck(computer_deck) < value_of_deck(user_deck):
                print("You have won!")
            else:
                print("Draw!")

            is_game_ended = True

    another_game = input("Do you want to play another game? Type 'y' for yes, 'n' for no: ").lower()

    if another_game == 'y':
        is_game_ended = False
        computer_deck.clear()
        user_deck.clear()
        print("\n" * 20)  # Clear the screen
        main()
    elif another_game == 'n':
        print("Thanks for playing!")


main()
