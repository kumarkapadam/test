"""def msg():
    print("hello welcome to functions")
msg()

a=20
def sum():
    a=10
    b=20
    c=a+b
    print("result is :",c)

sum()

a=35  # global
def outer_fun():
    #a=15  # enclosed

    def inner_fun():
       # a=10  # local
        b=20
        c=a+b
        print("c is :",c) # inbuIlt
    inner_fun()
print("helloo")

outer_fun()





def msg():
    pass
print(msg)


def sum(a,b):
    c = a+b
    return c
x = sum(2,3)
print("the result is :",x)


def outer_fun():
    #print("am in outer function ")
    def inner_fun():
        print("am in inner function")
        return "kumar"
    return inner_fun

print("hello")
print(outer_fun())


def hello():
    print("this is hello function")
    return 'helloo'
print(hello())




# function inside function


def outer_fun():
    print("this is outer function")
    return "outer_function"

print(outer_fun())
print("-------------------------------------")
print(outer_fun)


def sum_outer():
    a=10
    b=20
    c=a+b
    print("result c is :",c)
    def sum_inner():
        c=a-b
        return 'result subtraction c is:',c
    return sum_inner()


sum_outer()
print(sum_outer())


def hello_fun():
    print('this is hello function ')
    def hai_fun():
        print("this is hai function")
        return 'hai'
    return hai_fun()

print(hello_fun())


def sum(a, b):
    return a + b


print(sum)  # address of the object
print(sum())  # error  sum() missing 2 required positional arguments: 'a' and 'b'
print(sum(10, 20))


def msg(msg):
    return "hello hai {}".format(msg)

print(msg("kumar"))


def outer_fun():
    print("this is outer function ")
    def inner_fun():
        print("this is inner function")
    return inner_fun()

print(outer_fun())



def outer_function(func):
    print("this is outer_function")
    def inner_function():
        print("this is inner function")
        a=10
        b=20
        c=a+b
        return c
    func()
    return inner_function()
@outer_function
def main_func():
    print("this is main func")




outer_function(main_func)



def outer_function():
    message = 'hello hai'
    print("hai hello")
    def inner_message():
       print(message)
    return inner_message()

outer_function()


def decorator_function(original_function):
    def wraper_function():
        return original_function()

    return wraper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()



def add(msg):
    def wrapper_function():
        return msg()
    return wrapper_function

@add
def display():
    print("hello hai how are you")

display()



def div(a,b):
    print(a/b)
    #print("quetionent is",c)

def value(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
    return inner

obj1 = value(div)
obj1(4,10)

def add():
    a=10
    b=20
    c=a+b
    return c

def sub(func):
    def inner():
        a=10
        b=3
        d=a-b
        print("d is ",d)
        return func()
    return inner

obj1 = sub(add)
print(obj1())


def message(msg):
    print("hello welcome to :", msg)


def dis_msg(func):
    def update(msg1):
        print(msg1.upper())
        return func()

    return update


msg = dis_msg(message('python'))
print(msg('k'))




def update_msg(func):
    def inner(msg):
        print("executing ",func.__name__,"function")
        func(msg)
        print("execution completed")
    return inner
@update_msg
def message(msg):
    print("hello welcome ",msg)

message('python')
 """


def update_upper(func):
    def inner_upper():
        str1 = func()
        return str1.upper()

    return inner_upper


def update_capit(func1):
    def inner_capit():
        str2 = func1()
        return str2.capitalize()

    return inner_capit



@update_upper
@update_capit
def display():
    return "hello welcome to python programming language"


print(display())
