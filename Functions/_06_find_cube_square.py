# find cube/square of a number


'''
1. CRUD       -retrieve
2. STATE      - string / input()
3. BEHAVIOR   - + operator / for loop
'''

# 0. Mathematics 80%


# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

# 2. Algorithm  80%

print("--------2. Algorithm----------")

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")


def square(num):
    if num < 0:
        print("please enter positive number")
    if num > 0:
        print("square of a number is:", num ** 2)
        print("cube of a number is  :", num ** 3)


num1 = int(input("enter any number:"))
square(num1)

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")

# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
