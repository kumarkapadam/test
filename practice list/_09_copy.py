# P01 Req: sum of the elements in a list


'''
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->    |  =   +=    |   for
'''

# 0. Mathematics 80%
'''
1. Define the list
2. Take initial sum as 0
3. Start reading it. 
4. While reading each char, sum of the elements
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")
list = [1,2,3,4,5,6]
print("normal list is :",list)
list1 = list.copy()
print("list1 is        :",list1)

# 2. Algorithm  80%

print("--------2. Algorithm----------")
print(" ***   method-1 ------- copy() using ****")

num1 = [1,2,3,10,12,15,17]
num2 = num1.copy()
print("num1 is  :",num1)
print(" num2 is :",num2)

num1.append(100)
print("num1 is  :",num1)   # only num1 updated
print(" num2 is :",num2)


print("*** method-2 --- = equal symbol using ")
num3 = [100,200,300,400,500]
num4 = num3

print(" num3 is :",num3)
print(" num4  is :",num4)

num3.append(600)

print(" num3 is :",num3)  # both updated
print(" num4  is :",num4)



print(" method 3  using slicing operator ")

list5 = [1,2,3,4,5,6,7,8,10]
print(" list5 is :", list5)

list6  = list5[:]
print("list6 is ",list6)

list6.append(123)

print("list5 is :",list5)
print("list6 is :",list6)  # only one updated


print(" method-4 list inside list ")

list7 = [1,2,23,11,[10,12,13,146,123]]
list8 = list7.copy()

print(" list7 is :",list7)
print(" list 8 is :",list8)

list7[4][0] = 20
print("list7 is ", list7)  # both list  updated
print("list8 is ", list8)

# Reverse list of elements and print in upper case

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

print(" ********************   2. Algorithm            ********************")

print(" ********************   3 Using Functions       ********************")

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")

