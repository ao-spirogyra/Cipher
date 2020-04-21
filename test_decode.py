import unittest
import string
from decode import count_alphabets

class MainTest(unittest.TestCase):
    def test_count_alphabets(self):
        alphabets = list(string.ascii_lowercase)
        text = "triplemitsuisbanned"
        count_alphabets(text,alphabets)
        self.assertEquals()


if __name__ == "__main__":
    unittest.main()