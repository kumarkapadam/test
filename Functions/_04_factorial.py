'''
1. CRUD       -->  Retrieval
2. STATE      -->  integer
3. BEHAVIOR   -->   while
'''

print(" ******************   mathematics  ****************")
"""
1. Take a number from the user.
2. Initialize a factorial variable to 1.
3. Use a while loop to multiply the number to the factorial variable and then decrement the number.
4. Continue this till the value of the number is greater than 0.
5. Print the factorial of the number.
6. Exit.
"""

print(" *******************    using built_in_function    *******************")
import math

num = int(input("enter any number"))
print("factorial of a number", math.factorial(num))

print(" ******************    using functions ***************************")

print(" ******** method1 ********")


def fact(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    print("Factorial of the number is: ", fact)


num = int(input("Enter number:"))
fact(num)

print(" ******** method2 ********")


def factorial(num):  # function definition
    fact = 1
    for i in range(2, num + 1):  # for loop for finding factorial
        fact = fact * i
    return fact  # return factorial


number = int(input("Please enter any number to find factorial: "))
result = factorial(number)  # function call
print(f'The factorial of {number} is {result}')

print(" ******** method3 ********")


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


num = int(input("enter any number:"))
print("factorial is :", fact(num))
