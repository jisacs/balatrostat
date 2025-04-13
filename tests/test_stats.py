import unittest
from unittest.mock import Mock
from pokerstat.stats import get_stats
from pokerstat.Deck import Deck


class TestStats(unittest.TestCase):
    def test_get_stats_same_value(self):
        # Create mock cards with same value
        card1 = Mock(value='2')
        card2 = Mock(value='2')
        card3 = Mock(value='2')
        
        # Create a mock deck (not used in current implementation)
        deck = Mock()
        
        # Test with cards of same value
        result = get_stats([card1, card2, card3], deck)
        self.assertEqual(result, 1)

    def test_get_stats_different_values(self):
        # Create mock cards with different values
        card1 = Mock(value='2')
        card2 = Mock(value='3')
        card3 = Mock(value='4')
        
        # Create a mock deck
        deck = Mock()
        
        # Test with cards of different values - should raise AssertionError
        with self.assertRaises(AssertionError):
            get_stats([card1, card2, card3], deck)

    def test_get_stats_same_cards(self):
        # Create mock cards with same value
        card1 = Mock(value='2', suit='hearts')
        card2 = Mock(value='2', suit='hearts')
        card3 = Mock(value='2', suit='hearts')
        deck = Deck()
        
        # Test with cards of same value
        result = get_stats([card1, card2, card3], deck)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()