from pokerstat.Card import Card
import random
from constant import POKER_CONSTANTS

class Deck:
    def __init__(self, build=True):
        self.cards = []
        if build:
            self.build()
    
    def build(self):
        values = POKER_CONSTANTS.get_values()
        for suit in POKER_CONSTANTS.get_suits():
            for value in values:
                self.cards.append(Card(value, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, nb_cards=1):
        if nb_cards > len(self.cards):
            raise ValueError(f"Not enough cards in deck. Requested: {nb_cards}, Available: {len(self.cards)}")
        cards = [self.cards.pop(0) for _ in range(nb_cards)]
        return cards

    def is_empty(self):
        return len(self.cards) == 0

    def size(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __len__(self):
        return len(self.cards)