from random import shuffle

# TODO: This should go into a discard pile class
discardPiles = [1, 1, 100, 100]
directions = [1, 1, -1, -1]

# TODO: This should go into a draw pile class
cards = list(range(2, 100))
shuffle(cards)

validInput = False
numberOfPlayers = None
while not validInput:
    numberOfPlayers = int(input("Give me the number of players between 2 and 5: "))
    validInput = numberOfPlayers >= 2 and numberOfPlayers <= 5

# print cards before drawing
print("cards before drawing: " + cards.__str__())

numberOfCards = 6

hands = []
for playerIndex in range(0, numberOfPlayers):
    hands.append(cards[-numberOfCards:])
    cards = cards[:-numberOfCards]

print("discard piles" + discardPiles.__str__())
print("directions: " + directions.__str__())
print("cards: " + cards.__str__())
print("numberOfPlayers: " + numberOfPlayers.__str__())
print("numberOfCards: " + numberOfCards.__str__())
print("hands: " + hands.__str__())

