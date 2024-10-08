from random import shuffle
from enum import Enum

import inputconverters


class SetupSource:
    def read_number_of_players(self):
        pass

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
        return PlayerMove([SingleMove(2, 0), SingleMove(1, 0)])


class FixedSetupSource(SetupSource):
    def __init__(self, value=None):
        self.value = value

    def read_number_of_players(self):
        return self.value


class Direction(Enum):
    INCREASING = 1
    DECREASING = -1


class IllegalPlay(BaseException):
    pass


class DiscardPile:

    def __init__(self, direction: Direction, last: int):
        self.direction = direction
        self.last = last

    @staticmethod
    def from_direction(direction: Direction):
        return DiscardPile(direction, 1 if direction == Direction.INCREASING else 100)

    def __str__(self):
        return self.direction.name + " " + str(self.last)

    def __repr__(self):
        return str(self)

    def play(self, card):
        if (card - self.last) / self.direction.value <= 0 and not abs(card - self.last) == 10:
            raise IllegalPlay()
        return DiscardPile(self.direction, card)


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

        # check no cards are played multiple times
        used_cards = set(map(card, move.moves))
        assert len(used_cards) == len(move.moves)

        # check only available cards are played
        hand_size = len(self.hands[player])
        legal_cards = set(filter(lambda c: 0 <= c < hand_size, used_cards))
        assert len(legal_cards) == len(used_cards)

        # check cards are legal to play on pile

        print(move)

    def make_move(self, player: Player):
        move = player.make_move(self.hands[player], self.view_of_discard_piles())
        self.process(player, move)

    def __init__(self, players):
        self.players = players

        self.discard_piles = [DiscardPile.from_direction(Direction.INCREASING),
                              DiscardPile.from_direction(Direction.INCREASING),
                              DiscardPile.from_direction(Direction.DECREASING),
                              DiscardPile.from_direction(Direction.DECREASING)]

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
