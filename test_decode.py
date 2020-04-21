import unittest
from decode import splitTextToGroup

class MainTest(unittest.TestCase):
    def test_splitTextToGroup(self):
        text = "triple MITSU is banned"
        self.assertEqual(text,"triple MITSU is banned")
        print(text)
        text_list = list(text)
        length_of_key = 3
        group = splitTextToGroup(text, length_of_key)
        for i in range(length_of_key):
            x = 0
            for l in range(i,len(text),length_of_key):
                group[i][x] = text_list[l]
                text_list_counter = i + x
                self.assertEqual(text_list[text_list_counter],group[i][x])
                x += 1
                print(group[i][x])

if __name__ == "__main__":
    unittest.main()