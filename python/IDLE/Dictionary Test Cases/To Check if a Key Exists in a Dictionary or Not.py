# 1-Test Case to Check if a Key Exists in a Dictionary or Not

import sys
sys.path.append("D:\IDLE\DICTIONARY")
import unittest
import key_exists_dict

class TestKey(unittest.TestCase):
    def testcase(self):
        self.assertEqual(key_exists_dict.key_exists({"a":1,"b":2,"c":3}),("Exists"))

if __name__=="__main__":
    unittest.main()                         
