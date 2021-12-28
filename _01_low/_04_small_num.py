# Reverse list of elements and print in upper case

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

list1 = [10, 20, 1, 2, 3, 5, 12, 13, 46, 21, 33]
print("normal list  :", list1)
print('smaller number  in list :', min(list1))

print(" *** using sort() function  *****")

list2 = [10, 2, 3, 4, 5, 7, 98, 100, 12, 34]
print("list2 is   :", list2)
list2.sort()
print("sorted the list is :", list2)

print(" ********************   2. Algorithm            ********************")
list2 = [10, 2, 3, 4, 5, 7, 98, 100, 12, 34]
for i in range(len(list2)):
    for j in range(len(list2)):
        if list2[i] < list2[j]:
            list2[i], list2[j] = list2[j], list2[i]
print(list2)
print("ascending order :", list2)

print(" ********************   3 Using Functions       ********************")
list2 = []


def min_val(list2):
    for i in range(len(list2)):
        for j in range(len(list2)):
            if list2[i] < list2[j]:
                list2[i], list2[j] = list2[j], list2[i]
    return list2


num = int(input("enter how many numbers  to be inserted:"))
for i in range(num):
    elem = int(input("enter number"))
    list2.append(elem)
min_val(list2)
print("sorted list is    :", list2)
print("smaller number is :", list2[0])
print("biggest number is :", list2[-1])

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
