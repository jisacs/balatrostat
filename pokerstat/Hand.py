from pokerstat.Card import Card
import random

class Hand:
    def __init__(self, deck, nb_cards=1):
        self.cards = deck.deal(nb_cards)
        

