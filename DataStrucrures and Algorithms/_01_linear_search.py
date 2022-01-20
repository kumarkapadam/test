# datastructures ::
"""   way to store and organize the data so that it can be accessed effectively
built-in-datastructure :::
list
tuple
set
dictionary
string



user-defined datastructure
==========================
stack
queue
linked list
tree
graph

"""

# list
"""
list is collection of zero or many, separated by cpmma and enclosed with [].
you can  access list elements using indexing


"""
# linear search

list1 = [10, 20, 203, 40, 50, 60, 70, 80]
key = int(input("enter any key:"))
for i in list1:
    if key == i:
        print("key is found", i)
        break
else:
    print("key is not found")

print("----------------using range() -------------")
list1 = [10, 20, 203, 40, 50, 60, 70, 80]
key = int(input("enter any key:"))
for i in range(len(list1)):
    if key == list1[i]:
        print("key is found", list1[i], "index is ", i)
        break
else:
    print("key is not found")

print("---------------user functions-------------------")

list2 = []


def search(list2, key):
    for i in range(len(list2)):
        if key == list2[i]:
            print("key is found")
            break
    else:
        print("key is not found")


num = int(input("how many numbers do you want:"))
for i in range(num):
    elem = int(input("enter any number:"))
    list2.append(elem)
print("list2 is :", list2)
key = int(input("enter any key:"))
search(list2, key)

list2 = []
list3 = []
flag = False


def search(list2, key):
    for i in range(len(list2)):
        if key == list2[i]:
            flag = True
            list3.append(i)
    if flag == True:
        print("key is found ")
        for i in list3:
            print(i)
    else:
        print("key is not found")


num = int(input("how many numbers do you want:"))
for i in range(num):
    elem = int(input("enter any number:"))
    list2.append(elem)
print("list2 is :", list2)
key = int(input("enter any key:"))
search(list2, key)
print("======================================================================")

