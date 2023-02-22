# 1-Python Program to Find Largest Number in a List

  # 1Method
'''
list = [1,2,4,5,7,0]
list.sort()
print('largest number is:',list[-1])
'''
  # 2Method
'''
list = [1,5,0,6,8]
print('largest element is',max(list))
'''

  # 3Method
'''
lis=[3,4,16,5,2,3,9,7]
max=lis[0]
length=len(lis)
for i in range(1,length):
    if max<lis[i]:
        max=lis[i]
print(max)
'''

# 2-Python Program to Find Second Largest Number in a List

  # 1Method
'''
list=[10,20,34,42,11,23]
list.sort()
element = list[-2]
print("second largest number :", element)
'''
# 3-Python Program to Print Largest Even and Largest Odd Number in a List
'''
array=list(map(int,input().split()))
max_even=array[0]
max_odd=array[0]
length=len(array)
for i in range(1,length):
    if array[i]%2==0:
        array[i]>max_even
        max_even=array[i]
    elif array[i]%2==1:
        array[i]>max_odd
        max_odd=array[i]
print(max_even,max_odd)

'''

# 4-Python Program to Split Even and Odd Elements into Two Lists

'''
lis=list(map(int,input().split()))
even=[]
odd=[]
for i in lis:
    if i%2==0:
        even=even+[i]
    else:
        odd=odd+[i]
print(even)
print(odd)
'''
# 5-Python Program to Find Average of a List

  # 1Method
'''  
lis=[1,2,3,4,3,4]
sum=0

length=len(lis)
for i in lis:
    sum=sum+i
print(round((sum/length),2))
'''
  # 2Method
'''
num = [1,2,3,4,5,6,9]
average = sum(num)/len(num)
print("Average of list: ", round(average,3))
'''

# 6-Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List

'''
lis=list(map(int,input().split()))
negative_sum=0
even=0
odd=0
for i in lis:
    if i<0:
        negative_sum=negative_sum+i
    elif i>=0 and i%2==0:
        even=even+i
    elif i>=0 and i%2==1:
        odd=odd+i
print(negative_sum,even,odd)
'''


# 7-Python Program to Count Occurrences of Element in List

'''
n = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(n)
'''
# 8-Python Program to Find the Sum of Elements in a List using Recursion

'''
def sum(n,l):
    if l ==0:
        return 0
    else:
        return n[l-1]+sum(n,l-1)
n=list(map(int,input("enter ur list: ").split()))
l = len(n)
b = sum(n,l)
print(b)
'''

# 9-Python Program to Find the Length of a List using Recursion

'''
len = 0
def length(a):
   global len
   if a:
      len = len + 1
      length(a[1:])
   return len
a = [1, 2, 3, 4, 5, 6]
len = length(a)
print("The length of a list is", len)
'''



# 10-Python Program to Merge Two Lists and Sort it
'''
def merge():
    l1 = [1,2,3,4]
    l2 = [5,6,7,8]
    l = l1+l2
    print(l)
merge()    
    
'''

# 11-Python Program to Remove Duplicates from a List

   # 1Method
'''
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))
'''

# 12-Python Program to Swap the First and Last Element in a List

'''
list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)
'''
# 13-Python Program to Sort a List According to the Second Element in Sublist

# 14-Python Program to Return the Length of the Longest Word from the List of Words
# 15-Python Program to Find the Number Occurring Odd Number of Times in a List

# doubt
'''
lis=list(map(int,input().split()))
dict_a={}
for i in lis:
    if i not in dict_a:
        dict_a[i]=1
    else:
        dict_a[i]+=1
for key,values in dict_a.items():
    if values%2==1:
        print(key)
'''

# 16-Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

'''
import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)
'''

# 17-Python Program to Remove the ith Occurrence of the Given Word in a List
'''
lis=input().split()
n=int(input())
lis.remove(lis[n])
print(lis)
'''
# 18-Python Program to Find the Cumulative Sum of a List
'''
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
cum_list=[]   
y = 0  
for x in range(0,len(list)):  
    y+=list[x]  
    cum_list.append(y)   
      
print(cum_list)  
'''
# 19-Python Program to Find the Union of Two Lists

'''
list1 = [1, 2, 3, 4, 5, 6]
print("First list is:", list1)
list2 = [2, 4, 6, 8, 10, 12]
print("Second list is:", list2)
for element in list2:
    if element not in list1:
        list1.append(element)
print("Union of the lists is:", list1)
'''
# 20-Python Program to Find the Intersection of Two Lists

'''
x = [11, 23, 11, 2, 3, 4, 5]
y = [3, 11, 5, 2, 7, 23]

set1 = set(x)
set2 = set(y)

intersect = set1.intersection(set2)
result = list(intersect)

print(result)
'''

# 21-Python Program to Flatten a List without using Recursion

'''
n=[[1,2,3],[5,4,3,6]]
lis=[]
for i in n:
    lis=lis+i
print(lis)
'''

# 22-Python Program to Find the Total Sum of a Nested List Using Recursion
# 23-Python Program to Flatten a Nested List using Recursion

