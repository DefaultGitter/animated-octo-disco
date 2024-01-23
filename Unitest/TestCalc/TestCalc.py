from unittest import TestCase
from Unitest.Calc.prog import calc


class TestCalc(TestCase):
    def test_plus(self):
        # self.assertEqual(calc('2+2'), 4)
        self.assertEqual(calc('2+2'), 5)

    def test_minus(self):
        self.assertEqual(calc('5-2'), 1)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as ex:
            calc('22')
        self.assertEqual('does`nt found -+/*', ex.exception.args[0])
