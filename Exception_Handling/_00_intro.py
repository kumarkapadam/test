"""
the errors in the software are called bugs.and the process of removing them is called debugging.
"""
# Errors in a python program
"""
compile-time errors
runtime errors
logical errors

"""

# compile-time errors
"""syntactical errors found the code 

example : we forgot to write colon in the if statement , after the condition this will raise Syntax error

x=1
if x == 1   # SyntaxError: invalid syntax
    print("value is 1")

"""
try:
    num1 = int(input("enter any number :"))
    num2 = int(input("enter any number :"))
    num3 = num1 / num2
    print(" division   :", num3)

except ValueError:
    print("please enter integer numbers only")
except ZeroDivisionError:
    print("you enter b value is zero ")
    print("please enter positive value")

except Exception as e:
    print("error occurred ==", type(e))

print("**************************  key error   ****************************")

"""
dict1 = {'name': 'kumar', 'id': 27, 'loc': 'hyd'}
print("normal dictionary  :",dict1)
print("name :",dict1['name'])
print("company is :",dict1['company'])  # KeyError  """

try:
    dict1 = {'name': 'kumar', 'id': 27, 'loc': 'hyd'}
    print("normal dictionary  :", dict1)
    print("name :", dict1['name'])
    print("company is :", dict1['company'])
except KeyError as ke:
    print("key is not found in dictionary")

print(" ***********************  indentation error  *************************")

"""def add(x,y):

z=x+y    # indentation error
print("z value :",z)

add(10,20) """

print(" ***********************   value error  *****************************")

try:
    x = int(input("enter any number :"))
    print('x value is :', x)

except ValueError:
    print("please enter integers only")

pre_year = input("enter present year:")
birth_year = input("enter your birth year")

age = pre_year - birth_year
print(age)  # TypeError: unsupported operand type(s) for -: 'str' and 'str' """

print(" **************************  type error **************************")
try:
    pre_year = input("enter present year:")
    birth_year = input("enter birth year")
    age = pre_year - birth_year
except TypeError as ve:
    print("please enter integer type only")
    print("TypeError: unsupported operand type(s) for -: 'str' and 'str'", ve)
except Exception:
    print("exception occurred")
finally:
    print("end_program")

print("************************  zero division error ************************")

try:
    num1 = int(input("enter any number "))
    num2 = int(input("enter any number "))
    num3 = num1 / num2
    print("division is :", num3)
except ZeroDivisionError as zde:
    print("please enter denominator other than zero ")
except Exception:
    print(" error occurred ")




print("===================================================================================")
try:
    list = []
    num = int(input("enter how many numbers to be inserted:"))
    for i in range(num):
        elem = int(input("enter number"))
        list.append(elem)
    print("list is ",list)
    print("index of list",list[5])

except IndexError as ve:
    print("index out of the range ")

except Exception as e:
    print("error occurred ",type(e))

finally:
    print("*******   end_program   *******")



print("---------------raise exception---------------")

try:
    num = int(input(" enter any number :"))
    if num >= 0:
        if num == 0:
            print("zero")
        else:
            print(num, "is positive number")
    else:
        print(num, " is negative number")
except ValueError as ve:
    print("please enter integer number")
except Exception as e:
    print("error occurred ")
finally:
    print("end")


print("================================================")

try:
    num = int(input("enter any number:"))
except Exception as e:
    print("exception occurred")
else:
    if num >= 0:
        if num == 0:
            print("zero")
        else:
            print("positive number")
    else:
        print("negative number")
finally:
    print("end_program")

"""in above program in try block there is  no exceptions else block and finally block executed ,
in exception occurred in try block except block will be executed"""


def num():
    try:
        num = int(input("enter any number:"))
    except Exception:
        print("exception occurred")
    else:
        if num >= 0:
            if num == 0:
                print("zero")
            else:
                print("positive number")
        else:
            print("negative number")
    finally:
        print("end_program")


num()



try:
    n=int(input("Enter a number:"))
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
except Exception:
    print("exception occurred")
else:
    print("The total sum of digits is:",tot)

finally:
    print("end_program")








