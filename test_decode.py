import unittest
import string
from decode import count_alphabets
from decode import calculateIndexOfCoincidence

class MainTest(unittest.TestCase):
    def test_count_alphabets(self):
        alphabets = list(string.ascii_lowercase)
        text = "triplemitsuisbanned"
        num_of_alphabets = count_alphabets(text,alphabets)
        self.assertEqual(
            {
                'a': 1, 'b': 1, 'c': 0, 'd': 1, 'e': 2, 'f': 0, 'g': 0, 'h': 0, 'i': 3,
                'j': 0, 'k': 0, 'l': 1, 'm': 1, 'n': 2, 'o': 0, 'p': 1, 'q': 0, 'r': 1,
                's': 2, 't': 2, 'u': 1, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            },
            num_of_alphabets)

    def test_calculateIndexOfCoincidence(self):
        text = "triplemitsuisbanned"
        IC = calculateIndexOfCoincidence(text)
        self.assertEqual(13.26315789473684,IC)


if __name__ == "__main__":
    unittest.main()