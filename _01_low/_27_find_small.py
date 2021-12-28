print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")
list1 = [1, 10, 11, 12, 8, 3, 4, 11, 15, 5]
print("normal list :", list1)
list1.sort()
print(" list1 is :", list1)
print("second smaller number in list:", list1[-2])

print(" ********************   2. Algorithm            ********************")

list2 = [10, 2, 3, 4, 5, 7, 98, 100, 12, 34]
for i in range(len(list2)):
    for j in range(len(list2)):
        if list2[i] < list2[j]:
            list2[i], list2[j] = list2[j], list2[i]
print(list2)
print("ascending order :", list2)
print("second largest number in list:", list2[-2])
print("second smallest number in list:", list2[1])

print(" ********************   3 Using Functions       ********************")

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
