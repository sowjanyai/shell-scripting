# To Generate Random Numbers from 1 to 20 and Append Them to the List

import sys
sys.path.append("D:\IDLE\LIST")
import unittest
import generate_random_numbers

class Testrandom(unittest.TestCase):
    def testcase(self):
        self.assertEqual(random_num.random_num(),([20, 17, 9, 5, 11, 6, 15, 16, 13, 19]))
if __name__=="__main__":
    unittest.main()                         
