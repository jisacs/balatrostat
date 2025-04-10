from Card import Card
import random

class Deck:
    def __init__(self, build=True):
        self.cards = []
        if build:
            self.build()
    
    def build(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, nb_cards=1):
        cards = [self.cards.pop(0) for _ in range(nb_cards)]
        return cards