# 1-To Remove Odd Indexed Characters in a string

'''
string=input("enter the string:") 

res=""
for i in range(len(string)):
    if i%2==0:
     res+=string[i]
print(res)
'''

# 2-Python Program to Remove the nth Index Character from a Non-Empty String

'''
s=input("enter a string:")
n=int(input("enter the index:"))
first=s[:n]
last=s[n+1:]
new=first+last
print(new)
'''

# 3-Python Program to Replace All Occurrences of ‘a’ with $ in a String

'''

m=input()
str = m.replace('a', '$')
#print("Modified string : ")
print(str)
'''

# 4-Python Program to Replace Every Blank Space with Hyphen in a String

'''
m = input()
str = m.replace(' ','-')
print(str)
'''

# 5-Python Program to Reverse a String without using using slice

'''
string=input()
rev=[]
for i in string:
    rev=[i]+rev
print(rev) 
'''


# 6-Python Program to Determine How Many Times a Given Letter Occurs in a String
  # 1Method
'''
str = 'python'
letter='p'
print(str.count(letter))
'''
 # 2Method
''' 
count = 0
str = "Programiz"
letter = "r"
for i in str:
    if i == letter:
        count += 1
print(count)
'''

# 7-Python Program to Find the Length of a String without Library Function

'''
string=input("Enter string:")
count=0
for i in string:
    count=count+1
print("Length of the string is",count)

'''


# 8-Python Program to Count the Number of Words and Characters in a String

'''
string=input()
char=0
word=1
for i in string:
    char=char+1
    if(i==' '):
     word=word+1
print('num of words in string',word)
print('num of char in string',char)
''' 


# 9-Python Program to Count Number of Lowercase Characters in a String

'''
string=input()
count=0
for i in string:
    if(i.islower()):
        count=count+1
print("The number of lowercase characters is:")
print(count)
'''

# 10-Python Program to Count the Number of Vowels in a String

  # 1Method
'''
string = input()
vowels = ['a','e','i','o','u']
count = 0
for i in string:
    if i in vowels:
        count+= 1
print('num of vowels: ', count)
'''
 # 2Method
''' 
string =input()
vowels = 0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
         vowels=vowels+1
print('total num of vowels=',vowels) 
'''


# 11-Python Program to Count Number of Uppercase and Lowercase Letters in a String

'''
s=input()
upper=0
lower=0
for i in s:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper=upper+1
print('the upper letters are',upper)
print('the lower letters are',lower)
'''

# 12-Python Program to Count the Number of Digits and Letters in a String

'''
string=input()
digit=0
letter=0
for i in string:
    if(i.isdigit()):
        digit=digit+1
    letter=letter+1
print('num of digits',digit)
print('num of letters',letter)
'''

# 13-Python Program to Check if the Substring is Present in the Given String

'''
string = input('enter the string ')
for i in range(len(string)):
    for j in (i+1,len(string)+1):
    print(string[i:j])
'''

# 14-Python Program to Find Common Characters in Two Strings

'''
str1=input()
str2=input()
a=set(str1.split())
b=set(str2.split())
common=list(a.intersection(b))
print(common)
'''


# 15-Python Program to Print All Letters Present in Both Strings

'''
s1=input()
s2=input()
a=list(set(s1)|set(s2))
print('the letters are: ')
for i in a:
    print(i)
'''
# 16-Python Program that Displays which Letters are in First String but not in Second

'''
s1=input()
s2=input()
a=list(set(s1)-set(s2))
for i in a:
    print(a)
''' 

# 17-Python Program that Displays Letters that are not Common in Two Strings

'''
s1=input()
s2=input()
a=list(set(s1)^set(s2))
for i in a:
    print(i)
'''

# 18-Python Program to Create a New String Made up of First and Last 2 Characters

'''
string=input()
count=0
for i in string:
    count=count+1
new=string[0:2]+string[count-2:count]
print('newly made string', new)
'''

# 19-Python Program to Find the Larger String without using Built-in Functions



# 20-Python Program to Swap the First and the Last Character of a String

'''
string=input()
new_string=string[-1]+string[1:-1]+string[0]
print(new_string)
'''

# 21-Python Program to Count the Occurrences of Each Word in a String

'''
string=input()
word=input()
res=string.split()
count=0
for i in res:
    if i == word:
        count=count+1
print(count)
'''

 # 2Method
'''
string=input()
word=input()
count=string.count(word)
print(count)
'''

# 22-Python Program to Count Number of Vowels in a String using Sets

'''
string=input()
count=0
vowels=set('aeiou')
for i in string:    
    if i in vowels:
        count=count+1
print('num ofvowels', count) 
'''


# 23-Python Program to Check if a Given String is Palindrome

'''
n = int(input())
temp = n
rev = 0
while n >0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n //10
if rev == temp:
    print('palindrome')
else:
    print('not a palindrome')

'''
