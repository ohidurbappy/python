import unittest

from validation import validate_username


class TestValidateUsername(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(validate_username("validuser",3),True)

    def test_too_short(self):
        self.assertEqual(validate_username("me",3),False)

    def test_invalid_characters(self):
        self.assertEqual(validate_username("invalid_username",4),False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError,validate_username,"user",-1)

unittest.main()