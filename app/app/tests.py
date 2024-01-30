"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtracting numbers together"""
        res = calc.subtract(5, 6)
        self.assertEqual(res, -1)
