# Python Program to Remove Duplicates from a List


def duplicate(list):
    list1=[]
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1
list=[1,2,3,4,5,2,3,4,5,7,8,9,6,1]
list1=duplicate(list)
print("the list after removing duplicates:",list1)
