'''

1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  if ,elif,else
'''

print("******************  mathematics  ************************")
"""
1.take a 3 inputs from the user
2. and compare to the input values
3. finally maximum value is found.

"""


def maximum(a, b, c):
    if a >= b and a >= c:
        largest = a

    elif (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))
print("maximum number is :", maximum(a, b, c))
