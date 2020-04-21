import unittest
import string
from decode import count_alphabets

class MainTest(unittest.TestCase):
    def test_count_alphabets(self):
        text = "triple MITSU is banned"
        alphabets = list(string.ascii_lowercase)
        counter = count_alphabets(text,alphabets)
        self.assertEqual(counter,26)

if __name__ == "__main__":
    unittest.main()