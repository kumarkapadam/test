print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

list = [1, 10, 11, 12, 8, 3, 4, 11, 15, 5]
print("length of the list:", len(list))

print(" ********************   2. Algorithm            ********************")

list = [10, 14, 13, 17, 11, 15, 19, 11, 11, 13, 11]
count = 0
for i in list:
    count += 1
print("count of the list:", count)
print("how many times repeat 11 in list", list.count(11))

print("*** method-2 ****")
print("   specified indexes    ")
print("how many times repeat 13 in list :", list.count(13))

print(" using collections ")

from collections import Counter

MyList = ["m", "n", "m", "o", "o", "m", "o"]

duplicate_dict = Counter(MyList)

print(duplicate_dict)  # to get occurrence of each of the element.

print("\nNumber of Occurrences of m is the list: ", duplicate_dict['m'])

print(" ********************   3 Using Functions       ********************")

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
