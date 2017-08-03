# Is it unique: Implement an algorithm to determine if a string has all unique characters. Without additional data structure.
import unittest


# Without Data Structure O(N*Log(N))
# ================
def is_unique(s):
    s =sorted(s)
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True
#==========
# With Data Structure O(N)
def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True
    return True
#============
# Test
class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]
    def test_unique(self):
    # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)

    # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)
if __name__ == "__main__":
    unittest.main()
