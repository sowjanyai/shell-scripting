'''
def name(a,b):
    print(a,b)
name(1,2)
'''

'''
def name(a):
    print(a)
name("python")
'''

# single parameter
'''
def name(a):
    print("this is function",a)
name(':python')
'''

# multiple parameter
'''
def name(a,b):
    print("this is function",a,b)
name("-python",2)
'''

# return
'''
def name(a,b):
    return(a+b)
w=name(1,2)
print(w)
'''
'''
def name(a):
    return(a*3)
print(name(3))
'''

# arbitary argument (*a)
'''
def name(*a):
    print(a)
name(1,2,3)
'''

#Keyword argument-(kwargs) (**a)

'''
def name(**a):
    print(a)
name(name="python", value=1)
'''


'''
def name(a):
    for i in a:
        print(i)
name((1,2,3,4,5))
'''
'''
def name(a):
    return(a)
print(name("Hello World"))
'''

# 1-function with 2 arguments
'''
def add_nums(num1,num2):
    sum=num1+num2
    print("sum is:",sum)

add_nums(2,5)
'''
# or

'''
def add_nums(num1,num2):
    sum=num1+num2
    return(sum)
print(add_nums(1,2))
'''

# 2-function return type- square problem

'''
def square(num):
    result=num*num
    return(result)
print(square(3))
'''
# 3-library function
'''
import math
square=math.sqrt(4)
print(square)
power=pow(2,3)
print("2 to the power 3 is",power)
'''

# 4-To create a function that takes two arguments, name and age, and print their value.

'''
def fun_name(name,age):
    return(name,age)
print("sowjanya",24)

'''
# 5-To create function func1() to accept a variable length of arguments and print their value.

'''
def func1(*args):
    for i in args:
        print(i)
func1(20,39)
func1(56,89,90)
'''


# 6-to create function calculation() such that it can accept two variables and calculate addition and subtraction.
   # Also, it must return both addition and subtraction in a single return call.

'''
def calculation(a,b):
    add=a+b
    sub=a-b
    return(add,sub)
print(calculation(40,10))
'''

# 7-Write a program to create a function show_employee() using the following condition

  # It should accept the employee’s name and salary and display both.
  # If the salary is missing in the function call then assign default value 9000 to salary


'''
def show_employee(name,salary=9000):
    print("Name:",name, "salary:",salary)
show_employee("Ben",12000)
show_employee("jessa")
'''


# 8-Create an inner function to calculate the addition in the following way
   # Create an outer function that will accept two parameters, a and b
   # Create an inner function inside an outer function that will calculate the addition of a and b
   # At last, an outer function will add 5 into addition and return it

'''
# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)

'''

# 9-Assign a different name to function and call it through the new name

'''
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)
'''

# 10-Generate a Python list of all the even numbers between 4 to 30
'''
print(list(range(4,30,2)))
'''     

# 11- Define a function that accepts 2 values and return its sum, subtraction and multiplication.
'''
def num(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    print(f"sum is {sum},sub is {sub}, mul is {mul}")
a=int(input("Enter value of a:"))
b=int(input("Enter valuue of b:"))
num(a,b)
'''

# 12-Define a function that accepts roll number and returns whether the student is present or absent.
'''
def details(roll):
    x=[2,3,4,5]
    if roll in x:
        print(f"Roll number is {roll} present")
    else:
        print(f"Roll number is {roll} absent")

roll=int(input("enter roll no:"))
details(roll)
'''

# 13-Define a function in python that accepts 3 values and returns the maximum of three numbers.
'''
def max(a,b,c):
    if a>b and a>c:
        print(f"{a} is max among all")
    elif b>a and b>c:
        print(f"{b} is max among all")
    else:
        print(f"{c} is max among all")

max(10,33,22)
'''

# 14-Define a function that accepts a number and returns whether the number is even or odd.
'''
def func(x):
    if x % 2 == 0:
        print(f"{x} is Even number")
    else:
        print(f"{x} is Odd number")
x = int(input("Enter a number "))
func(x)
'''

# 15- Define a function which counts vowels and consonant in a word.

'''
def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con + 1

    print("Count of vowels is ",vov)
    print("Count of consonant is ",con)

x = input("Enter Value: ") # pythonlobby
count(x)
'''

# 16-Define a function that returns Factorial of a number.

'''
def fact(num):
    fact=1
    while(num!=0):
        fact *= num
        num = num - 1
    print('factorial is',fact)
num=int(input())
fact(num)
'''
# 17-Define a function that accepts lowercase words and returns uppercase words.
'''
def response(text):
    z = text.upper()
    print(z)

text = input()  
response(text)
'''

# 18-Write a Python function to sum all the numbers in a list.
'''
def sum(num):
    total=0
    for i in num:
        total+=i
    return total
print(sum((8,2,3,0,7)))
'''

# 19-Write a Python function to multiply all the numbers in a list
'''
def mul(num):
    total=1
    for i in num:
        total*=i
    return total
print(mul((8,2,3,-1,7)))
'''

# 20-Python function that accepts a string and calculate the number of upper case letters and lower case letters.
'''
def string(s):
    d={"upper_case":0,"lower_case":0}
    for c in s:
        if c.isupper():
            d["upper_case"]+=1
        elif c.islower():
            d["lower_case"]+=1
        else:
            pass
    print("no of upper case characters :",d["upper_case"])
    print("no of lower case characters :",d["lower_case"])
s=input()
string(s)
'''


def string(s):
    x={"lower_case":0,"upper_case":0}
    for i in x:
        if i.islower():
            x["lower_case"]+=1
        elif:
            x["upper_case"]+=1
        else:
            pass
    print("no of lower case :",x["lower_case"]
    print("no of upper case :",x["upper_case"
            





































  













