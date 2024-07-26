from random import shuffle
from enum import Enum


class DiscardPile:
    def __init__(self, direction):
        self.direction = direction
        self.last = 1 if direction == Direction.INCREASING else 100

    def __str__(self):
        return self.direction.name + " " + str(self.last)

    def __repr__(self):
        return str(self)


class Direction(Enum):
    INCREASING = 1
    DECREASING = -1


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
    result = []
    for playerIndex in range(0, numberOfPlayers):
        result.append(deck[-numberOfCards:])
        for cardIndex in range(0, numberOfCards):
            deck.pop(len(deck) - 1)
    return result


discardPiles = [DiscardPile(Direction.INCREASING), DiscardPile(Direction.INCREASING), DiscardPile(Direction.DECREASING),
                DiscardPile(Direction.DECREASING)]

cards = list(range(2, 100))
shuffle(cards)

numberOfPlayers = read_number_of_players()

numberOfCards = calculate_number_of_cards_per_player(numberOfPlayers)

hands = draw_hands(cards)

print("discard piles: " + str(discardPiles))
print("cards: " + str(cards))
print("numberOfPlayers: " + str(numberOfPlayers))
print("numberOfCards: " + str(numberOfCards))
print("hands: " + str(hands))
