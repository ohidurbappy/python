from geometry import square
import unittest

class TestSquare(unittest.TestCase):
    def test_basic(self):
        test_case=3
        expected=9
        self.assertEqual(square(test_case),expected)

    def test_edge(self):
        test_case=0
        expected=0
        self.assertEqual(square(test_case),expected)
    
    def test_empty(self):
        test_case=''
        expected=''
        self.assertEqual(square(test_case),expected)

    def test_negative(self):
        test_case=-5
        expected=25
        self.assertEqual(square(test_case),expected)
unittest.main()