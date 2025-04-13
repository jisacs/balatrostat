import unittest
from pokerstat.stats import proba_exactement_N_valeurs

class TestStats(unittest.TestCase):
    def test_proba_exactement_N_valeurs(self):
        # Test impossible cases
        self.assertEqual(proba_exactement_N_valeurs(5, 5), 0.0)  # Can't get 5 cards when there are only 4 of a kind
        self.assertEqual(proba_exactement_N_valeurs(3, 2), 0.0)  # Can't get 3 cards when drawing only 2
        self.assertEqual(proba_exactement_N_valeurs(2, 53), 0.0)  # Can't draw more than 52 cards

        # Test getting exactly 2 cards of a kind when drawing 5 cards
        # There are 4 cards of the kind we want and 48 other cards
        # We want to get 2 of the kind and 3 of the others
        prob = proba_exactement_N_valeurs(2, 5)
        self.assertAlmostEqual(prob, 0.03992981808107859, places=4)

        # Test getting exactly 1 card of a kind when drawing 3 cards
        prob = proba_exactement_N_valeurs(1, 3)
        self.assertAlmostEqual(prob, 0.2041266968325792, places=4)

        # Test getting exactly 4 cards of a kind when drawing 5 cards
        prob = proba_exactement_N_valeurs(4, 5)
        self.assertAlmostEqual(prob, 0.00001846897415730337, places=4)

        # Test with different total cards and number of values
        prob = proba_exactement_N_valeurs(2, 3, total_cartes=32, nb_valeurs=2)
        self.assertAlmostEqual(prob, 0.006048387096774194, places=4)

if __name__ == '__main__':
    unittest.main()