"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test the adding numbers together."""

        res = calc.add(5,6)
        #print(help(calc.add))

        self.assertEqual(res,11)

    def test_substract_numbers(self):
        '''Test substracting numbers'''
        
        res = calc.substract(10,15)

        self.assertEqual(res, 5)