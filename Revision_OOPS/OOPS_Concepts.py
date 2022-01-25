"""
class and object
================
class is a design from the object
class is a design
class is a blueprint

class is a collection of objects






class Computer:
    def config(self):
        print("computer configuration")


com1 = Computer()
com1.config()

class Student:
    def stu_info(self):
        print("student name is :",'kumar')

stu1 = Student()
stu1.stu_info()

Student.stu_info(stu1)


"""
"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def stu_det(self):
        print(f' student name is :', self.name,"and age is :", self.age)


stu1 = Student('kumar',25)
stu1.stu_det()
Student.stu_det(stu1) 

"""

# __init__

# special variables ===> __name__
# special methods  ====> __init__

# self


# constructor


# size of an object
"""
depends on the number of variables and size of each variable
"""

# types of variables
"""
1. instance variable:
======================
Instance variables: If the value of a variable varies from object to object, then such variables are called instance variables.



2. class variable or ( static variable)
Class Variables:     A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.




# types of methods
===================
1. class methods
=================


2.instance methods
==================



3.static methods
===================









"""


class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return self.m1 + self.m2 + self.m3


s1 = Student(50, 60, 70)
print(s1.avg())

s2 = Student(59, 78, 90)
print(s2.avg())

# accessors   getters === fetch the value

# mutators   setters===> modified the value


# inner class
"""
class inside a class

 """


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


stu1 = Student('kumar', 30)
stu1.show()

lap1 = Student.Laptop()
lap1.show()

print("=================== class =========================")


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = 'kumar'
emp1.last = 'k'
emp1.email = "kkr@gmail.com"
emp1.pay = 30000

print(emp1.email)

print("=========using init=================")


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + 'last' + '@gmail.com'

    def emp_det(self):
        print(self.first, self.last, self.pay, self.email)


emp1 = Employee('kumar', 'k', 30000)
emp1.emp_det()

print("=========== class variable ===========")


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('kumar', 'k', 30000)

print(emp1.fullname())



print("============= class variable ==========================")
class Student:
    # Class variable
    school_name = 'JNTUH '

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


# create first object
s1 = Student('kumar', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('yuvi', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)


print("============ accesing class variable ============================")



class Student:
    # Class variable
    school_name = 'JNTU HYD '

    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('kumar k')