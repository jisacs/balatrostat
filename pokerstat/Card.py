class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        suit_icons = {
            'Hearts': '♥',  # Red
            'Diamonds': '♦',  # Red
            'Clubs': '♣',  # Black
            'Spades': '♠'   # Black

        }
        icon = suit_icons.get(self.suit, self.suit)  # Fallback to suit name if not found
        return f"[{self.value}{icon}]"