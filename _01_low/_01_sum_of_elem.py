# P01 Req: sum of the elements in a list

print("*********************   0.Mathematics          *********************")
'''
1. Define the list
2. Take initial sum as 0
3. Start reading it. 
4. While reading each char, sum of the elements
'''

print("*********************   1. Builtin Functions   *********************")
list1 = [10, 20, 30, 40, 50]  # static way
print("sum of the list : ", sum(list1))

print(" ********************   2. Algorithm            ********************")
print("****** method1 ********")
list1 = [10, 20, 30, 40, 50]
sum1 = 0
for i in list1:
    sum += i
print("sum of the list is:", sum1)

print("****** method2 ********")

sum1= 0
list2 = []
num = int(input('enter how many numbers to be inserted:'))
for i in range(num):
    elem = int(input("enter number :"))
    list2.append(elem)
print("list2   is  :", list2)

for i in list2:
    sum += i
print(" sum of the list is :", sum)

print(" ********************   3 Using Functions       ********************")

list2 = []


def sum_list(list):
    sum1 = 0
    for i in list2:
        sum1 += i
    print(" sum of the list is :", sum1)


num = int(input('enter how many numbers to be inserted:'))
for i in range(num):
    elem = int(input("enter number :"))
    list2.append(elem)
print("list2   is  :", list2)
sum_list(list2)

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
