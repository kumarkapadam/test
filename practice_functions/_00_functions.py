"""def outer_fun():
    def inner_fun():
        print("hello this is inner function")
    print("hello this is outer function")
    inner_fun()
outer_fun()



def outer_function():
    message = "hai"
    def inner_function():
        print(message)
    return inner_function
my_func = outer_function()
my_func()




def func(string):
    def wrapper():
        print("start")
        print(string)
        print("end")
    return wrapper()

x = func('hello')
print(x)



# iterators

num = [1,2,3,4,5]
print("nums is :", num)
num1 = iter(num)
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))


def sum():
    for i in range(1,10):
        yield i

s = sum()
for i in s:
    print(i)


def outer_fun():
    def inner_fun():
        print("hello this is inner function")
    print("hello this is outer function")
    inner_fun()

outer_fun()



def message(msg):
    message = "hello"
    def message1():
        print(message)
    return message1()

message()



def message(msg):
    def wrapper():
        print("start")
        print(msg)
        print('end')
    return wrapper
x= message('hello')
x()



def outerfunction():

    def inner_fun():
        print("this is outer function")
    print("ths is innerfunction")
    return inner_fun()

outerfunction()


def message(display):
    def inner_msg():
        print(display)
    return inner_msg

def display():
    print("hello welcome ")

msg = message(display)
msg()


class Computer():
    def __init__(self):
        return "hello"   # type error
    def process(self):
        print("hello welcome")

com1 = Computer()
com1.process()

from abc import ABC , abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("hello this is the process")



com1 = Laptop()
com1.process()
"""

