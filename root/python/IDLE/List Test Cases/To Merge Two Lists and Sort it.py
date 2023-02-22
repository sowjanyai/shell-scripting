# Test Case to Merge Two Lists and Sort it

import sys
sys.path.append("D:\IDLE\LIST")
import unittest
import merge_two_lists
class TestMerge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_two_lists.merge(),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__=="__main__":
    unittest.main()
