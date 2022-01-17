# print the following floating numbers with no decimal places

import math

num1 = float(input('Enter num1 : '))
num2 = float(input('Enter num2 : '))


def no_decimal(n1, n2):
    print('the value with no decimal', math.trunc(n1))
    print('the value with no decimal', math.trunc(n2))
    print('the value with no decimal', round(n1))
    print('the value with no decimal', round(n2))
    print('the value with no decimal', int(n1))
    print('the value with no decimal', int(n2))


no_decimal(num1, num2)
