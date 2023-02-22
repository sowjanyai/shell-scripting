# TestCase to Find Average of a List

import sys
sys.path.append("D:\IDLE\LIST")
import unittest
import average_of_list
class TestAvg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(average_of_list.list_avg([1,2,3,4,5,6],3.5))
if __name__=="__main__":
    unittest.main()
