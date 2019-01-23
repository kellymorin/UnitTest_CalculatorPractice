import unittest
import sys
sys.path.append('../')
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests
        self.calc = Calculator()
        self.num1 = 2
        self.num2 = 6

    @classmethod
    def tearDownClass(self):
        print('Tear down class')


    def test_add(self):
        result = self.calc.add(2, 7)
        expected = 9
        self.assertEqual(result, expected)
        self.assertNotEqual(self.calc.add(3, 3), 4)
        self.assertEqual(self.calc.add(self.num1, self.num2), 8)
        # with self.assertRaises(ValueError):
            # self.calc.add('s', 's')

    def test_subtract(self):
        result = self.calc.subtract(7, 2)
        expected = 5
        self.assertEqual(result, expected)
        self.assertNotEqual(self.calc.subtract(3, 3), 4)

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        expected = 6
        self.assertEqual(result, expected)
        self.assertNotEqual(self.calc.multiply(3, 3), 12)

    def test_divide(self):
        result = self.calc.divide(4, 2)
        expected = 2
        self.assertEqual(result, expected)
        self.assertNotEqual(self.calc.divide(9, 3), 4)

  # Write test methods for subtract, multiply, and divide


if __name__ == '__main__':
    unittest.main()