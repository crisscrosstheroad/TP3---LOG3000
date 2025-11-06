import unittest
from app import calculate

class TestApp(unittest.TestCase):

    def test_valid_expressions(self):
        """Vérifie que calculate retourne le bon résultat pour des expressions valides de chaque calcul arithmétique supporté."""
        self.assertEqual(calculate("2 + 3"), 5)
        self.assertEqual(calculate("10 - 4"), 6)
        self.assertEqual(calculate("3 * 2"), 6)
        self.assertEqual(calculate("8 / 2"), 4)

    def test_invalid_expressions(self):
        """Vérifie que calculate indique une erreur pour des expressions invalides."""
        with self.assertRaises(ValueError):
            calculate("2 ++ 3")
        with self.assertRaises(ValueError):
            calculate("")
        with self.assertRaises(ValueError):
            calculate("a + 3")