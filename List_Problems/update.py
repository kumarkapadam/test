list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list1:
    print(i)

for i in range(len(list1)):
    print(i)

i = 0
while i < len(list1):
    i += 1
print()

print("list1 is :", list1)
print(list1[0])
print(list1[1])
list1[1:3] = 10, 11
print(list1)

list1[4] = 111
print("updated list is :", list1)

print("**********************************    elements in reverse order    *****************************")
names = ['kumar', 'kiran', 'raju', 'veera', 'shiva']
print("names is ", names)

for i in names:
    print(i)

for i in enumerate(names, start=1):
    print(i)

i = 0
while i < len(names):
    print(names[i])
    i += 1
print()

print(" ********  reverse ********")

names = ['kumar', 'kiran', 'raju', 'veera', 'shiva']
i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1

print(" ********* repetition of list **************")

names = ['kumar', 'kiran', 'raju', 'veera', 'shiva']
print(names * 3)

# membership operator

print('kumar' in names)  # True
print('kiran' in names)
print('veera' in names)
print('shiva' in names)
print('ravi' in names)  # False

# cloning list

x = [1, 2, 3, 4, 5, 6]
y = x
print("x is :", x)  # x is : [1, 2, 3, 4, 5, 6]
print("y is :", y)  # y is : [1, 2, 3, 4, 5, 6]

x.append(10)
print("updated x is :", x)
print("y is :", y)

y.append(11)
print("y is :", y)

print("============================================================================================")
"""
sum()  : list.sum()  :: returns sum of all elements in the list
index() : list.index(x)  :: returns the first occurrence of xin the list 
append() : list.append(x) :: appends x at the end of the list
insert() : list.insert(i,x) :: insert x in to the list in the position specified by i
copy()  : list.copy()  copies all the list in the position specified by i
extend()  list.extend(list1)    appends list1 to list
count() :;  list.count(x)  :: returns number of occurences of x in the list
remove() :: list.remove(x) :: removes x from the list
pop()   :: list.pop()  ::  removes the ending elements from the list 
sort()  ::  list.sort()  :: sorts the elements of the list into ascending order
reverse()  ::  list.reverse()   teverses the sequences  of elements in the list
clear()  :; list.clear() :: deletes all elements from the list 
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers is :", num)
print("length of numbers is :", len(num))

# append
num.append(123)
print("updated number is :", num)

num.append('kumar')
print("updated number is :",num)


num.extend(['umar'])
print(num)


print(" ************    bubble sort   ****************")

list1 = [10,9,1,2,6,8,4]
print("list1  is :", list1)

for i in range(1,len(list1)):
    for j in range(1,len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
        print(list1)