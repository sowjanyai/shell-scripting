# 1-what is tuple

'''
  A Tuple is an immutable objects, which means it cannot be changed, and we use it to represent fixed collections of items.
  ( ) --> empty tuple
  (1.0,9.9,10) --> a tuple containing numeric objects
  ('abc','hello','aws') --> a tuple containing string
  ('10',101,True) --> a tuple containing a string,an integer,and boolean)
  a_tuple = (0,[1,2,3],(4,5,6),7.0)
  print(a_tuple)
'''

# 2-What is the key difference between tuples and lists?

'''
  The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable.
  therefore, it is possible t change a list but not a tuple.
  The contents of a tuple cannot change nce they have been created in python due to the immutability of tuples.
'''

  
# 3-Reverse the tuple

'''
tuple=(1,2,'python','java',23.1,11,12)
rev=tuple[::-1]
print(rev)
'''

  # Using reverse()
'''
n=(1,2,'python','java',23.1,11,12)
rev=reversed(n)
print(tuple(rev))
'''
   
# 4-Access value 20 from the tuple  tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

'''
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
'''

# 5-Unpack the tuple into 4 variables tuple1 = (10, 20, 30, 40)

'''
tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print(a,b,c,d)
'''

# -Swap two tuples in Python  tuple1 = (1,2),tuple2 = (3,4)

'''
tuple1 = (1,2)
tuple2 = (3,4)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)
'''

# 7-Write a program to modify the first item (22) of a list inside a following tuple to 22
    # tuple1 = (11, [11, 33], 44, 55)

'''
tuple1 = (11, [11, 33], 44, 55)
tuple1[1][0]=22
print(tuple1)
'''
    
# 8-Sort a tuple of tuples by 2nd item
   # tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))



# 9-Counts the number of occurrences of item 10 from a tuple1 = (50, 10, 60, 70, 10)

'''
tuple1 = (50, 10, 60, 70, 10)
print(tuple1.count(10))
'''

# 10-Check if all items in the tuple are the same tuple1 = (10, 10, 10, 10)




# 11-Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

'''
list=[2,3,4,5]
tuplelist = []
for i in list:
    myTuple = (i, (i*i))
    tuplelist.append(myTuple)
print(str(tuplelist))
'''

# 12-Write a Python program to find the repeated items of a tuple

'''
tuple=(1,2,3,2,3,4,5,6)
print(tuple)
count=tuple.count(2)
print(count)
'''

# 13-Write a Python program to convert a tuple to a list

'''
tuple=(1,'asc',123,1.2,'asd')
res=list(tuple)
print(res)
'''

# 14-Write a Python program to convert a tuple to a dictionary
  # t = (("Name", "Ram"),("Age", 23),("City", "Bangalore"),("Marks", 422))

'''
t = (("Name", "Ram"),("Age", 23),("City", "Bangalore"),("Marks", 422))
res=dict(t)
print(res)
'''
   
# 15-Write a Python program to get unique elements in nested tuple
   # val = [(1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,)]

'''
val = [(1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,)]
res = []
s = set()
for i in val:
    for j in i:
        if not j in s:
            s.add(j)
            res.append(j)
print(res)            
'''
