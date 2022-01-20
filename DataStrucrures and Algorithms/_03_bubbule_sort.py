# sinking sort
"""it is a simple sorting algorithm  which sorts n number of elements in the list by comparing the each pair of adjusent items"""

list1 = [10,11,18,4,3,1]
print("normal list  is :", list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
         if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
         else:
             print(list1)
    print()

print("sorted list is :", list1)