# 1-Python Program to Remove Odd Indexed Characters in a string
'''
string=input("enter the string: ")
res=""
for i in range(len(string)):
    if i%2==0:
        res+=string[i]
print(res)
'''

   # In functions

'''
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

'''
