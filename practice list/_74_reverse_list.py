# Reverse list of elements and print in upper case


'''
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->    |  =   +=    |   for
'''

# 0. Mathematics 80%
'''

'''

print("-----1. Builtin Functions--------")

list1 = [1, 2, 3, 4, 10, 11, 12, 'hello', 'kumar']
print("normal list      :", list1)
print("reverse of list  :", list1[::-1])

list2 = ['k', 'u', 'm', 'a', 'r']
print("normal list is   :", list2)
print("reversed list is :", list2[::-1])
x = list2[::-1]
y = (str(x).upper())
print("upper elements is :", y)

print(" ********* reverse()  **********")

num = [12, 3, 12, 46, 84]
print(" numbers is    :", num)
num.reverse()
print("reversed numbers :", num)

print(" ********************    2. Algorithm  **************************")

rev_list = [1,2,3,5,10,122,'hello','kumar',(1,2,3,4)]
print("normal list is   :",rev_list)

print("reversed list is :",rev_list[::-1])




for i in reversed(rev_list):
    print(i,end=" ")
print()




list  = ['kumar','kiran','shiva','yuvi']

for i in reversed(list):
     upper = i.upper()
     print(upper)

print("normal list is ",list)


print("--------3 Using Functions----------")

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")

# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
