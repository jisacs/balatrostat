class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        suit_icons = {
   'Hearts': '\033[31m♥\033[0m',  # Red
            'Diamonds': '\033[31m♦\033[0m',  # Red
            'Clubs': '\033[30m♣\033[0m',  # Black
            'Spades': '\033[30m♠\033[0m'   # Black

        }
        icon = suit_icons.get(self.suit, self.suit)  # Fallback to suit name if not found
        return f"[{self.value}{icon}]"