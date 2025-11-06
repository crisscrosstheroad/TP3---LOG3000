import unittest
from operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):

    def test_add(self):
        """Vérifie que la fonction add retourne la somme correcte de deux nombres."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """Vérifie que la fonction subtract retourne la différence correcte."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(0, -3), 3)

    def test_multiply(self):
        """Vérifie que la fonction multiply retourne le produit correct."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(2, 0), 0)

    def test_divide(self):
        """Vérifie que la fonction divide retourne le résultat de la division correct et gère la division par zéro."""
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(5, 0)