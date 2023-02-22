# Python Program to Split Even and Odd Elements into Two Lists

def split_lists(list):
    even=[]
    odd=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

list=[1,2,3,4,5,6,7,8,9]
even,odd=split_lists(list)
print("even elements:",even)
print("odd elements:",odd)


