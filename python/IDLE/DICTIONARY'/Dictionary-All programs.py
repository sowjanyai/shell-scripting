# 1-Python Program to Check if a Key Exists in a Dictionary or Not

'''
dict={'a':1,'b':2,'c':3}
n = input()
if n in dict:
    print('Exists')
else:
    print('Not exists')
'''

# 2-Python Program to Add a Key-Value Pair to the Dictionary

'''
dict={'a':1,'b':2,'c':3}
dict['d']=4
print(dict)
'''

# 3-Python Program to Find the Sum of All the Items in a Dictionary

'''
dict_a={"a":10,"b":11,"c":22,"d":33}
sum=0
for value in dict_a.values():
    sum=sum+value
print(sum)
'''
  #2Method
'''
dict={'a':10,'b':20,'c':30,'d':40}
print(sum(dict.values()))
'''

# 4-Python Program to Multiply All the Items in a Dictionary

'''
dict_a={"a":10,"b":20,"c":30}
mul=1
for value in dict_a.values():
    mul=mul*value
print(mul)
'''

# 5-Python Program to Remove a Key from a Dictionary

'''
dict={"a":11,"b":23,"c":22}
del dict["b"]
print(dict)
'''

# 6-Python Program to Concatenate Two Dictionaries

'''
dict={"a":11,"b":23,"c":22}
dict1={1:'abc',2:'cvb'}
dict.update(dict1)
print(dict)
'''

# 7-Python Program to Map Two Lists into a Dictionary

'''
list=["name","domain","compony"]
list1=["soowjanya","devops","Msys"]
dict_a={}
length=len(list)
for i in range(length):
    dict_a[list[i]]=list1[i]
print(dict_a)
'''


# 8-Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

'''
m=input().split()
dict={}
for i in m:
    if i not in dict:
        dict[i]=i[0]
print(dict)
'''

# 9-Python Program to Count the Frequency of Each Word in a String using Dictionary

    


# 10-Python Program to clear the items from a Dictionary

'''
dict={"a":11,"b":23,"c":22}
res=dict.clear()
print(dict)
'''

# 11-Python Program to add a record to nested dictionary
'''
   people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
          2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
'''
# 12-Python Program to delete a record from nested dictionary
'''
   people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
          2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
'''
# 13-Python Program to copy from one dictionary to another

# 14-How to get min and max keys corresponding to min and max value in Dictionary
     fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
'''     
remove no value items from Dictionary
    mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
    
filter dictionary where the value is less than 20000.
    empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
    
How can you sort dictionary elements based on keys

    d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
    
How can you sort the dictionary elements based on values

    d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
'''
