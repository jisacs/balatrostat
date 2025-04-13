"""
Constants for the poker game
"""

# Card suits and values
SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Card value rankings (for comparisons)
VALUE_RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

# Card suit rankings (for comparisons)
SUIT_RANKS = {
    'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4
}

# Special hand rankings (for poker hands)
HAND_RANKS = {
    'High Card': 0,
    'Pair': 1,
    'Two Pair': 2,
    'Three of a Kind': 3,
    'Straight': 4,
    'Flush': 5,
    'Full House': 6,
    'Four of a Kind': 7,
    'Straight Flush': 8,
    'Royal Flush': 9
}

class PokerConstants:
    """Class to provide access to poker game constants"""
    
    @staticmethod
    def get_suits():
        """Return list of all card suits"""
        return SUITS
    
    @staticmethod
    def get_values():
        """Return list of all card values"""
        return VALUES
    
    @staticmethod
    def get_value_rank(value):
        """Get the rank number of a card value"""
        return VALUE_RANKS.get(value, 0)
    
    @staticmethod
    def get_suit_rank(suit):
        """Get the rank number of a card suit"""
        return SUIT_RANKS.get(suit, 0)
    
    @staticmethod
    def get_hand_rank(hand_name):
        """Get the rank number of a poker hand"""
        return HAND_RANKS.get(hand_name, 0)
    
    @staticmethod
    def get_hand_name(rank):
        """Get the name of a poker hand from its rank"""
        for name, r in HAND_RANKS.items():
            if r == rank:
                return name
        return None
    
    @staticmethod
    def is_valid_suit(suit):
        """Check if a suit is valid"""
        return suit in SUITS
    
    @staticmethod
    def is_valid_value(value):
        """Check if a card value is valid"""
        return value in VALUES
    
    @staticmethod
    def is_valid_hand(hand_name):
        """Check if a poker hand name is valid"""
        return hand_name in HAND_RANKS

# Create an instance for easy access
POKER_CONSTANTS = PokerConstants()

