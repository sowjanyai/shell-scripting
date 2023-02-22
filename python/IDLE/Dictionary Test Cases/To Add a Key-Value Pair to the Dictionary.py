# Test Case To Add a Key-Value Pair to the Dictionary

import sys
sys.path.append("D:\IDLE\DICTIONARY")
import unittest
import add_key_value
class Testaddkey(unittest.TestCase):
    def testcase(self):
        self.assertEqual(add_key_value.key_value({"a":1,"b":2,"c":3}),({'a': 1, 'b': 2, 'c': 3, 'd': 4}))


if __name__=="__main__":
    unittest.main()
