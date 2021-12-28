# Multiply of elements

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

print(" ********************   2. Algorithm            ********************")

print("****** method1 ********")

list1 = [1, 2, 3, 4, 5]
mul = 1
for i in list1:
    mul *= i
print("multiply  of the list is:", mul)

print("****** method2 ********")

mul = 1
list2 = []
num = int(input('enter how many numbers to be inserted:'))
for i in range(num):
    elem = int(input("enter number :"))
    list2.append(elem)
print("list2   is  :", list2)

for i in list2:
    mul *= i
print(" sum of the list is :", mul)

print(" ********************   3 Using Functions       ********************")

list2 = []


def mul_list(list):
    mul = 1
    for i in list2:
         mul *= i
    print(" sum of the list is :", mul)


num = int(input('enter how many numbers to be inserted:'))
for i in range(num):
    elem = int(input("enter number :"))
    list2.append(elem)
print("list2   is  :", list2)
mul_list(list2)






print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
