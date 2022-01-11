"""
A sequnce is a datatype thar represents a group of elements.
in python , strings , lists, tuple and dictionaries are sequence data types.
all sequences allow some common operations like indexing and slicing.


a list is similar to array that consists of a group of elemnts or items.
one major difference between array and a list.
an array can store only one type of elements where as a lsit can store different type of elements


"""
list1 = ['kumar', 'veera', 'raju']
print("list1 is :", list1)

# create a list  with different types of elements
num = [10, 20, 30, 40, 50, 60]
print("numbers is :", num)

float_num = [10,12,12.9,12,15.9]
print("float number is :", float_num)
print("type of the list is :",type(float_num))


mix_list = ['kumar',24.6,240000]
print('mixed list is :',mix_list)
print("mixed type of list is :",type(mix_list))


# create a list using range
for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)


# a python program  to create lists using range() function

list1 = range(5)
for i in list1:
    print(i," ",end =' ')
print()


print("======================================================================")
# a python program to access list elements using loops

list1 = [10,20,30,40,50,60,70,80]
i = 0
while i < len(list1):
    print(list1[i])
    i+=-1
print()

