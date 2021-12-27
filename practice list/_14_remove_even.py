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

# Reverse list of elements and print in upper case

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

print(" ********************   2. Algorithm            ********************")
num = []
for i in range(1, 100):
    if i % 2 == 0:
        continue
    else:
        num.append(i)
print("remove even_numbers")
print("numbers in list :", num)

print(" ********************   3 Using Functions       ********************")

even = []


def rem_even(list1):
    for i in list1:
        if i % 2 == 0:
            pass
        else:
            even.append(i)


list1 = []
num = int(input("enter how many numbers to be inserted "))
for i in range(num):
    elem = int(input("enter element :"))
    list1.append(elem)
print("list is :", list1)
rem_even(list1)
print("removing even numbers in list :", even)

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
