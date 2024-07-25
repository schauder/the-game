# This should go into a discard pile class
discardPiles = [1, 1, 100, 100]
directions = [1, 1, -1, -1]

cards = list(range(2, 100))

validInput = False
numberOfPlayers = None
while not validInput:
    numberOfPlayers = int(input("Give me the number of players between 2 and 5: "))
    validInput = numberOfPlayers >= 2 and numberOfPlayers <= 5

print(discardPiles)
print(directions)
print(cards)
print(numberOfPlayers)

