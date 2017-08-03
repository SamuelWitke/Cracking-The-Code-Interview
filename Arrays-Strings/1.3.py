# Replace All String with '%20'
import unittest


def urlify(s,length):
    end_index = len(s)
    for i in reversed(range(length)):
        if s[i] == ' ':
            s[end_index - 3:end_index] = '%20'
            end_index -= 3 
        else:
            s[end_index -1] = s[i]
            end_index -=1
    return s
class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [(list('much ado about nothing      '), 22,list('much%20ado%20about%20nothing')),
            (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
