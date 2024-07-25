from random import shuffle


def calculate_number_of_cards_per_player(number_of_players):
    if number_of_players == 1:
        return 8
    if number_of_players == 2:
        return 7
    return 6


def read_number_of_players():
    valid = False
    number_of_players = None
    while not valid:
        number_of_players = int(input("Give me the number of players between 1 and 5: "))
        valid = 1 <= number_of_players <= 5
    return number_of_players


def draw_hands(deck):
    hands = []
    for playerIndex in range(0, numberOfPlayers):
        hands.append(deck[-numberOfCards:])
        for cardIndex in range(0, numberOfCards):
            deck.pop(len(deck) - 1)
    return hands


# TODO: This should go into a discard pile class
discardPiles = [1, 1, 100, 100]
directions = [1, 1, -1, -1]

# TODO: This should go into a draw pile class
cards = list(range(2, 100))
shuffle(cards)

numberOfPlayers = read_number_of_players()

numberOfCards = calculate_number_of_cards_per_player(numberOfPlayers)

hands = draw_hands(cards)

print("discard piles" + discardPiles.__str__())
print("directions: " + directions.__str__())
print("cards: " + cards.__str__())
print("numberOfPlayers: " + numberOfPlayers.__str__())
print("numberOfCards: " + numberOfCards.__str__())
print("hands: " + hands.__str__())
