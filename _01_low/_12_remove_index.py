# Remove specified index from list and print

# Reverse list of elements and print in upper case

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")
print(" ****** method-1  ******")
print("Use del and specify the index of the element you want to delete:")
print(" and also support slicing ")
list1 = [1, 2, 33, 4, 6, 7, 8, 9, 10]
del list1[0]
print(" after deleting list is :", list1)  # [2, 33, 4, 6, 7, 8, 9, 10]

del list1[1:3]
print(" after using slicing  after deleted list is :",
      list1)  # [2, 6, 7, 8, 9, 10]

print("**** method2  ****")
print(" using pop ")
list2 = [1, 2, 33, 4, 6, 7, 8, 9, 10]
print("updated list is :", list2.pop())  # return the element
print(list2)

print("particular index will be deleted :", list2.pop(2))
print(list2)

print(" ********************   2. Algorithm            ********************")
list2 = [1, 2, 33, 4, 6, 7, 8, 9, 10]
list3 = []
print(len(list2))
for i in range(len(list2)):
    if i == 0:
        pass
    else:
        list3.append(list2[i])

print(list3)
print(" ********************   3 Using Functions       ********************")


def remove_index(list4):
    list5 = []
    for i in range(len(list4)):
        if i == 0:
            pass
        else:
            list5.append(list4[i])
    return list5


list4 = [10, 12, 1, 2, 3, 5, 6, 8, 9, 11]
ob = remove_index(list4)
print(ob)

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
