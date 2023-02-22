# To Split Even and Odd Elements into Two Lists

import sys
sys.path.append("D:\IDLE\LIST")
import unittest
import split_even_odd_list
class TestSplitEO(unittest.TestCase):
    def testcase(self):
        self.assertEqual(split_even_odd_list.split_lists([1,2,3,4,5,6,7,8,9]),([2, 4, 6, 8],[1, 3, 5, 7, 9]))

if __name__=="__main__":
    unittest.main()                        
                        
        
