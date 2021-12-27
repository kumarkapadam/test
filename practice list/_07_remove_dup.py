# remove duplicate elements in list
print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

list1 = [1, 10, 2, 3, 1, 2, 5, 7, 8, 5]
print("list is  :", list1)
print("remove duplicate elements:", list(set(list1)))

print(" ********************   2. Algorithm            ********************")

print(" ***** method-1 *****")
list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
list2 = []
list3 = []
for i in list:
    if i not in list2:
        list2.append(i)
    else:
        list3.append(i)
print(" after removing , list  is   :", list2)
print(" duplicates elements  is :", list3)

print(" **** method 2 ****")

"""
list1  = [1,2,3,4,1,2,3]
list = list(dict.fromkeys(list1))
print(list)  """
print(" ********************   3 Using Functions       ********************")

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
