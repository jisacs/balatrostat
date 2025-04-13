from typing import List, Optional
from random import shuffle
from pokerstat.Card import Card
from pokerstat.constant import POKER_CONSTANTS

class Deck:
    """
    Represents a deck of playing cards.
    
    Attributes:
        cards (List[Card]): List of cards in the deck
    """
    
    def __init__(self, cards: Optional[List[Card]] = None):
        """
        Initialize a new deck.
        
        Args:
            cards (Optional[List[Card]]): Initial cards to populate the deck with
        """
        self.cards = cards or []

    @classmethod
    def create_standard_deck(cls) -> 'Deck':
        """
        Create a standard 52-card deck.
        
        Returns:
            Deck: A new deck with all standard cards
        """
        return cls([Card(value, suit) 
                   for suit in POKER_CONSTANTS.get_suits() 
                   for value in POKER_CONSTANTS.get_values()])

    def shuffle(self) -> None:
        """
        Shuffle the deck randomly.
        """
        shuffle(self.cards)

    def deal(self, nb_cards: int = 1) -> List[Card]:
        """
        Deal cards from the deck.
        
        Args:
            nb_cards (int): Number of cards to deal
            
        Returns:
            List[Card]: Dealt cards
            
        Raises:
            ValueError: If not enough cards are available
        """
        if nb_cards > len(self.cards):
            raise ValueError(f"Not enough cards in deck. Requested: {nb_cards}, Available: {len(self.cards)}")
        return [self.cards.pop(0) for _ in range(nb_cards)]

    def is_empty(self) -> bool:
        """
        Check if the deck is empty.
        
        Returns:
            bool: True if deck is empty, False otherwise
        """
        return not self.cards

    def size(self) -> int:
        """
        Get the number of cards in the deck.
        
        Returns:
            int: Number of cards in the deck
        """
        return len(self.cards)

    def __str__(self) -> str:
        """
        Return a string representation of the deck.
        
        Returns:
            str: Deck description
        """
        return f"Deck of {len(self.cards)} cards"

    def __len__(self) -> int:
        """
        Return the number of cards in the deck.
        
        Returns:
            int: Number of cards in the deck
        """
        return len(self.cards)

    def __bool__(self) -> bool:
        """
        Return True if the deck is not empty.
        
        Returns:
            bool: True if deck is not empty
        """
        return bool(self.cards)

    def __iter__(self):
        """
        Make the deck iterable.
        """
        return iter(self.cards)

    def __getitem__(self, index):
        """
        Allow accessing cards by index.
        
        Args:
            index: Index of the card to access
            
        Returns:
            Card: The card at the specified index
            
        Raises:
            IndexError: If index is out of range
        """
        return self.cards[index]

    def __setitem__(self, index, card: Card):
        """
        Allow setting cards by index.
        
        Args:
            index: Index to set
            card: Card to place at the index
            
        Raises:
            IndexError: If index is out of range
        """
        self.cards[index] = card

    def __delitem__(self, index):
        """
        Allow deleting cards by index.
        
        Args:
            index: Index of card to delete
            
        Raises:
            IndexError: If index is out of range
        """
        del self.cards[index]