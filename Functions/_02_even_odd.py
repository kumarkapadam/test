# P01 Req: sum of the elements in a list


"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->    |  =   %    |   for
"""

#  Using Functions
print("-------- Using Functions----------")
even = []
odd = []


def even_odd(list1):
    for i in list1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)


list1 = []
num = int(input("enter how many numbers to be inserted:"))
for j in range(num):
    elem = int(input("enter number"))
    list1.append(elem)
print("list is :", list1)
even_odd(list1)
print("even numbers :", even)
print('odd numbers:', odd)
