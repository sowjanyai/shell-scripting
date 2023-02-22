# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

import random
def random_num():
    a=[]
    for i in range(10):
        a.append(random.randint(1,20))

    return a
print("generate random numbers", random_num())
