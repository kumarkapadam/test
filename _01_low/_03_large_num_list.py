# large number in list
print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")
list1 = [10, 11, 17, 100, 14, 6, 123, 112, 12, 674, 453, 567]
print("normal list is :", list1)
print("largest number in list :", max(list1))
print("smaller number in list :", min(list1))

print(" ********************   2. Algorithm            ********************")

list1 = [10, 11, 17, 100, 14, 6, 123, 112, 12, 674, 453, 567]
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)
print("min to max(ascending order is)",list1)
print("maximum value  is            :",list1[-1])
print("minimum value  is            :",list1[0])
print(" ********************   3 Using Functions       ********************")

list2 = []


def max_val(list2):
    for i in range(len(list2)):
        for j in range(len(list2)):
            if list2[i] < list2[j]:
                list2[i], list2[j] = list2[j], list2[i]
    return list2


num = int(input("enter how many numbers  to be inserted:"))
for i in range(num):
    elem = int(input("enter number"))
    list2.append(elem)
max_val(list2)
print("sorted list is    :", list2)
print("smaller number is :", list2[0])
print("biggest number is :", list2[-1])





print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
