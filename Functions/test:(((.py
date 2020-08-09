import unittest
from Functions.colk import Calculator

add = [[1, 1, 2], [10, 10, 20], [1, 2, 3], [2, 1, 3], [1, 0, 1], [0, 1, 1], [0, 0, 0], [-1, -1, -2], [-1, 0, -1]]

minus = [[1, 1, 0], [10, 10, 0], [1, 2, -1], [2, 1, 1], [1, 0, 1], [0, 1, -1], [0, 0, 0], [-1, -1, 0], [-1, 0, -1]]

mult = [[1, 1, 1], [10, 10, 100], [1, 2, 2], [2, 1, 2], [1, 0, 0], [0, 1, 0], [0, 0, 0], [-1, -1, -1], [-1, 0, 0]]

div = [[1, 1, 1], [10, 10, 1], [1, 2, 0.5], [2, 1, 2], [1, 0, 0], [0, 1, 0], [0, 0, 0], [-1, -1, 1], [-1, 0, 0]]


class CalculatorTest(unittest.TestCase):
    calc = Calculator()

    def test_act_add(self):
        calc = Calculator()
        for plus in add:
            result = calc.act('+', plus[0], plus[1])
            self.assertEqual(result, plus[2])

    def test_act_minus(self):
        calc = Calculator()
        for x in minus:
            result = calc.act('-', x[0], x[1])
            self.assertEqual(result, x[2])

    def test_act_mult(self):
        calc = Calculator()
        for x in mult:
            result = calc.act('*', x[0], x[1])
            self.assertEqual(result, x[2])

    def test_act_div(self):
        calc = Calculator()
        for x in div:
            result = calc.act('/', x[0], x[1])
            self.assertEqual(result, x[2])





            result = calc.act('*', x[0], x[1])
            self.assertEqual(result, x[2])

#     1+1 10+10 1+2 2+1 1+0 0+1 0+0 -1+-1 -1+0 -1+1 1.1+1 1.1+-1 1.1+2 1.1+0 1.1+0.9
