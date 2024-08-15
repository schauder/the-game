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


class SingleMove:
    def __init__(self,  card: int, pile: int):
        self.card = card
        self.pile = pile


class PlayerMove:
    def __init__(self, moves: [SingleMove]):
        self.moves = moves


class Player:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Player: " + self.name

    def __repr__(self):
        return self.__str__()

    def make_move(self, hand, piles) -> PlayerMove:
        print("Making a move for " + self.name)
        print(str(hand))
        print(str(piles))
        return PlayerMove([SingleMove(0, 0), SingleMove(1, 0)])


class FixedSetupSource(SetupSource):
    def __init__(self, value=None):
        self.value = value

    def read_number_of_players(self):
        return self.value


class Direction(Enum):
    INCREASING = 1
    DECREASING = -1


class DiscardPile:
    def __init__(self, direction: Direction):
        self.direction = direction
        self.last = 1 if direction == Direction.INCREASING else 100

    def __str__(self):
        return self.direction.name + " " + str(self.last)

    def __repr__(self):
        return str(self)


class DiscardPileView:
    def __init__(self, direction: Direction, last: int):
        self.direction: Direction = direction
        self.last: int = last

    def __str__(self):
        return self.direction.name + " " + str(self.last)

    def __repr__(self):
        return str(self)


def calculate_number_of_cards_per_player(number_of_players):
    if number_of_players == 1:
        return 8
    if number_of_players == 2:
        return 7
    return 6


class Game:
    cards = list(range(2, 100))
    shuffle(cards)
    hands = {}

    def draw_hands(self, number_of_hand_cards):
        result = {}
        for player in self.players:
            result[player] = self.cards[-number_of_hand_cards:]
            del self.cards[-number_of_hand_cards:]
        return result

    def process(self, player: Player, move: PlayerMove):

        def card(m: SingleMove):
            return m.card

        # check no cards a played multiple times
        assert len(set(map(card, move.moves))) == len(move.moves)

        # check only available cards are played
        # check cards are legal to play on pile
        print(move)

    def make_move(self, player: Player):
        move = player.make_move(self.hands[player], self.view_of_discard_piles())
        self.process(player, move)

    def __init__(self, players):
        self.players = players

        self.discard_piles = [DiscardPile(Direction.INCREASING), DiscardPile(Direction.INCREASING),
                              DiscardPile(Direction.DECREASING),
                              DiscardPile(Direction.DECREASING)]

        number_of_players = len(self.players)

        number_of_cards = calculate_number_of_cards_per_player(number_of_players)

        self.hands = self.draw_hands(number_of_cards)

        for player in self.players:
            self.make_move(player)

        print("discard piles: " + str(self.discard_piles))
        print("cards: " + str(self.cards))
        print("numberOfPlayers: " + str(number_of_players))
        print("number_of_cards: " + str(number_of_cards))
        print("hands: " + str(self.hands))
        print("players: " + str(self.players))

    def view_of_discard_piles(self):
        result = []
        for pile in self.discard_piles:
            result.append(DiscardPileView(pile.direction, pile.last))
        return result
