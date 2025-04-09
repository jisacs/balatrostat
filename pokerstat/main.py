from Deck import Deck
from Hand import Hand

deck = Deck()
deck.shuffle()

hand = Hand(deck, 10)
print(hand.cards)
