# To access index of list

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for index, value in enumerate(list1, start=0):
    print(index, value)
print()

names = ['kumar', 'kiran', 'yuvi', 'shiva', 'karthik']
print("index  is :", names.index('kumar'))

for i in names:
    print(i)

for index, i in enumerate(names):
    print(index, i)

print(" ********************   2. Algorithm            ********************")

for i in range(len(list1)):
    print(i, end=' ')
    print(list1[i])

names = ['kumar', 'kiran', 'yuvi', 'shiva', 'karthik']
print("  start ")
for i in range(len(names)):
    print(i, names[i])

print(" ********************   3 Using Functions       ********************")

print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
