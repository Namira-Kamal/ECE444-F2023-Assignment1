import unittest
from utils import formatter, reversed  #functions are in a file named utils.py

class TestUtils(unittest.TestCase): "Test cases for reversed and formatter functions"

    # Tests for the reversed function
    def TestReversed_ints(self):
        self.assertEqual(reversed(34567), 76543)
        self.assertEqual(reversed(-12345), -54321)
    
    def TestReversed_strings(self):
        with self.assertRaises(TypeError): "Not an int - assertRaises checks error paths"
            reversed("namira")

    def TestReversed_floats(self):
        with self.assertRaises(TypeError):"Not an int"
            reversed(341.45)

    # Tests for the formatter function
    def TestFormatter_ints(self):
        self.assertEqual(formatter(6), {"binary": "110", "octal": "6"})
    
    def TestFormatter_strings(self):
        with self.assertRaises(TypeError): "Not an int"
            formatter("kamal")
    
    def TestFormatter_floats(self):
        with self.assertRaises(TypeError): "Not an int"
            formatter(123.45)

if __name__ == '__main__':
    unittest.main()
