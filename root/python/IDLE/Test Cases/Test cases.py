# 1-Python Program to Remove Odd Indexed Characters in a string

'''
import unittest

class TestRemoveOdd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(str)
        
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

if __name__=="__main__":
    unittest.main()
'''

# Python Program to Find Common Characters in Two Strings

'''
import unittest

class Testsubstr(unittest.TestCase):
    def testcase(self):
        self.assertEqual(substring('test','cases'),(['t', 'e', 's', 't']))

def substring(s1,s2):
    a = list(set(s1).union(set(s2)))
    print("common characters:",a)
    return a

s1 = 'karun'
s2 = 'kumar'
print(substring(s1,s2))

if __name__=="__main__":
    unittest.main()
'''

# fibnocci

'''
import unittest

class Testfibnocci(unittest.TestCase):
    def testcase(self):
        self.assertEqual(fibnocci(8),"Fib")
if __name__=="__main__":
    unittest.main()
'''

# True or False

'''
import unittest

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

'''



# Python code to demonstrate working of unittest
'''
import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        pass

    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual( 'a'*4, 'aaaa')

    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')

    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # Returns true if the string is stripped and
    # matches the given output.
    def test_strip(self):        
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
'''
# Find list of max even and odd values

'''
import unittest
class find_max_evenodd(unittest.TestCase):
    def test_value1(self):
        self.assertEqual(Max_evenodd([266,306,299,99,100,201,555,206,302]),(306,555))
def Max_evenodd(list):
    list1 = []
    list2 = []
    even_max = 0
    odd_max = 0
    for i in list:
        if i % 2 == 0:
            list1.append(i)
            list1.sort()
            even_max = list1[-1]
     
        else:
            list2.append(i)
            list2.sort()
            odd_max = list2[-1]
    
    return even_max,odd_max


list = [266,306,299,99,100,201,555,206,302]

print("Maximun even & odd values is: ",Max_evenodd(list))

        
if __name__ == "__main__":
    unittest.main()

'''
