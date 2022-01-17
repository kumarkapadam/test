# taking a number as input and separating the number using comma separator
'''
CRUD : Update
State : Int
Behaviour : .format

Taking a input as any number and using format method formatting the number into comma separated value

'''

x = int(input('enter a number:'))
y = int(input('enter a number:'))
print("Before formatting1: ", x)
print("after formatting with comma separator:  " + "{:,}".format(x))
print("Before formatting: ", y)
print("after formatting with comma separator:  " + "{:,}".format(y))

x = int(input('enter a number:'))
y = int(input('enter a number:'))


def comma_sep(a, b):
    print("Before formatting1: ", a)
    print("after formatting with comma separator:  " + "{:,}".format(a))
    print("Before formatting: ", b)
    print("after formatting with comma separator:  " + "{:,}".format(b))


comma_sep(x, y)
