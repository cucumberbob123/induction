import unittest
from minibus import calculateMinibusNeeded as calculate


class TestMinibusCalculator(unittest.TestCase):
    def testFew(self):
        self.assertEqual(calculate(3, 15, 50), 1)

    def testMany(self):
        self.assertEqual(calculate(2, 20, 30), 0)

    def testExact(self):
        self.assertEqual(calculate(4, 10, 40), 0)


if __name__ == '__main__':
    unittest.main()
