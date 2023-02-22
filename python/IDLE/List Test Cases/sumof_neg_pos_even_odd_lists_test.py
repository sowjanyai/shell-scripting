
import sys
sys.path.append("D:\IDLE\LIST")
import unittest

import sumof_neg_pos_even_odd_lists

class Testsum(unittest.TestCase):
    def testcase(self):
        self.assertEqual(sumof_neg_pos_even_odd_lists.sum_list([-23,-45,23,56,87,32,-90]),(-158,198,88,110))

if __name__=="__main__":
    unittest.main()
