from random import shuffle
from enum import Enum

import numbers


class SetupSource:
    def read_number_of_players(self):
        pass


class StdinSetupSource(SetupSource):
    def read_number_of_players(self):
        number_of_players = None
        while number_of_players is None:
            number_of_players = numbers.safe_convert_to_int(input("Give me the number of players between 1 and 5: "))
            if number_of_players is None or number_of_players < 1 or number_of_players > 5:
                number_of_players = None
        return number_of_players


class FixedSetupSource(SetupSource):
    def __init__(self, value=None):
        self.value = value

    def read_number_of_players(self):
        return self.value


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


def draw_hands(deck, number_of_players, cards):
    result = []
    for playerIndex in range(0, number_of_players):
        result.append(deck[-cards:])
        for cardIndex in range(0, number_of_players):
            deck.pop(len(deck) - 1)
    return result


def start(setup_source=StdinSetupSource()):
    discard_piles = [DiscardPile(Direction.INCREASING), DiscardPile(Direction.INCREASING),
                    DiscardPile(Direction.DECREASING),
                    DiscardPile(Direction.DECREASING)]

    cards = list(range(2, 100))
    shuffle(cards)

    number_of_players = setup_source.read_number_of_players()

    number_of_cards = calculate_number_of_cards_per_player(number_of_players)

    hands = draw_hands(cards, number_of_players, number_of_cards)

    print("discard piles: " + str(discard_piles))
    print("cards: " + str(cards))
    print("numberOfPlayers: " + str(number_of_players))
    print("number_of_cards: " + str(number_of_cards))
    print("hands: " + str(hands))


class Game:
    pass
