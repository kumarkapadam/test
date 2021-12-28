'''

1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  for
'''



"""
1. Take in a number and store it in a variable.
2. Print the multiplication tables of a given number.
3. Exit.
"""

def table(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

num=int(input("Enter the number to print the tables for:"))
table(num)