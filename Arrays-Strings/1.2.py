#Given Two Strings Determine If one is a permutation of the other.
#O(N)
import unittest
def is_permutation(s):
    a = s[0]
    b = s[1]
    b_dic = {}
    for i in range(len(b)):
        b_dic[b[i]] = 0 
    if(len(a) != len(b)):
        return False
    else:
        for i in range(len(a)):
            if b_dic.get(a[i]) == None:
                return False
        return True

class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
        (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]
    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = is_permutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

