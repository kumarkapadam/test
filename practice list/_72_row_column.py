# Two digits m (row) and n (column) as input and generates a two-dimensional
# array. The element value in the i-th row and j-th column
# of the array should be i*j

print("*********************   0.Mathematics          *********************")

print("*********************   1. Builtin Functions   *********************")

print(" ********************   2. Algorithm            ********************")
print(" *****   method1   ******")
m = int(input("Row:"))
n = int(input("Column:"))
matrix = [[0 for col in range(n)] for row in range(m)]
for row in range(m):
    for col in range(n):
        matrix[row][col] = row * col
print(matrix)

print(" *****   method2   ******")
m = int(input("enter the rows : "))
n = int(input("enter the columns : "))
for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(i * j, end="  ")
    print()

print(" ********************   3 Using Functions       ********************")





row = int(input("enter rows:"))
col = int(input("enter cols:"))
row_col0




print(" ********************   4 Object Oriented       ********************")

print(" ********************   5 Exception handling   ********************")

print(" ********************   6 File Handling         ********************")

print(" ********************   7 Database interaction  ********************")

print(" ********************   8 UI Interaction       ********************")
