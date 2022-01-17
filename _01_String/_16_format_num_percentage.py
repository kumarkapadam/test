# Formatting a number with the percentage

'''
CRUD : Update
State : int
Behaviour : .format(), +

Taking the  number as user input and passing ti .format method to convert to percentage

'''

x = int(input('enter a number:'))
y = int(input('enter a number:'))
print("Before formatting: ", x)
print(" Number after formatting with percentage: " + "{:.2%}".format(x))
print("Before formatting: ", y)
print(" Number after formatting with percentage: " + "{:.2%}".format(y))

x = int(input('enter a number:'))
y = int(input('enter a number:'))


def format_to_percentage(a, b):
    print("Before formatting: ", a)
    print(" Number after formatting with percentage: " + "{:.2%}".format(a))
    print("Before formatting: ", b)
    print(" Number after formatting with percentage: " + "{:.2%}".format(b))


format_to_percentage(x, y)
