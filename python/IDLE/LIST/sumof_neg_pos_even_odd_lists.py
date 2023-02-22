# Python program to print sum of negative numbers, positive even and odd
# Numbers in a List
'''
import unittest
class sum_neg_pos_even_odd(unittest.TestCase):
    def test_list(self):
        self.assertEqual(sum_list([-23,-45,23,56,87,32,-90]),(-158,198,88,110))
'''
def sum_list(list1):
    Neg=0
    Pos=0
    Even=0
    Odd=0
    for i in list1:
        if i<0:
            Neg=Neg+i
        else:
            Pos=Pos+i
            if i%2==0:
                Even=Even+i
            else:
                Odd=Odd+i
    return (Neg,Pos,Even,Odd)
list1=[-23,-45,23,56,87,32,-90]
s=sum_list(list1)

print("the sum of neg pos even odd is:",s[0],s[1],s[2],s[3])

'''
if __name__=="__main__":
    unittest.main()
'''
