# Test case to Remove Duplicates from a List

import sys
sys.path.append("D:\IDLE\LIST")
import unittest
import remove_duplictae_from_list

class TestDuplicate(unittest.TestCase):
    def testcase(self):
        self.assertEqual(remove_duplictae_from_list.duplicate([1,2,3,4,5,2,3,4,5,7,8,9,6,1]),([1, 2, 3, 4, 5, 7, 8, 9, 6]))
if __name__=="__main__":
    unittest.main()
