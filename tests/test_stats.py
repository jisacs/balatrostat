import unittest
from pokerstat.stats import (proba_exactement_N_valeurs,
                            proba_exactement_N_valeurs_incomplete_game)

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


    def test_proba_exactement_N_valeurs_incomplete_game(self):
        # Test impossible cases
        self.assertEqual(proba_exactement_N_valeurs_incomplete_game(5, 5, 40, 3), 0.0)  # Can't get 5 cards when there are only 3 of a kind
        self.assertEqual(proba_exactement_N_valeurs_incomplete_game(3, 2, 40, 3), 0.0)  # Can't get 3 cards when drawing only 2
        self.assertEqual(proba_exactement_N_valeurs_incomplete_game(2, 41, 40, 3), 0.0)  # Can't draw more than 40 cards

        # Test with 40-card deck and 3 cards of each value
        prob = proba_exactement_N_valeurs_incomplete_game(2, 5, 40, 3)
        self.assertAlmostEqual(prob, 0.0343646183740216, places=2)

        # Test with 60-card deck and 5 cards of each value
        prob = proba_exactement_N_valeurs_incomplete_game(2, 5, 60, 5)
        self.assertAlmostEqual(prob, 0.04803459003076026, places=2)

        # Test getting exactly 1 card of a kind in a 40-card deck with 3 cards of each value
        prob = proba_exactement_N_valeurs_incomplete_game(1, 3, 40, 3)
        self.assertAlmostEqual(prob, 0.20243, places=2)

        # Test getting exactly 3 cards of a kind in a 60-card deck with 5 cards of each value
        prob = proba_exactement_N_valeurs_incomplete_game(3, 5, 60, 5)
        self.assertAlmostEqual(prob, 0.0002719149770728978, places=2)

        # Test with custom deck size and number of values
        prob = proba_exactement_N_valeurs_incomplete_game(2, 4, 36, 4)
        self.assertAlmostEqual(prob, 0.05089473684210526, places=2)


if __name__ == '__main__':
    unittest.main()