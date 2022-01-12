# Constructors in Python

"""Constructors are generally used for instantiating an object. The task of constructors is
to initialize(assign values) to the data members of the class when an object of the
class is created. In Python the __init__() method is called the constructor and is always
called when an object is created.
Syntax of constructor declaration :
def _init_(self)

"""
print("---------------------default constructor------------------")


class Mobile:
    def __init__(self):  # default constructor
        self.name = "redme"  # self.name ,self.ram , self.color all are instance variables
        self.ram = "4gb"  # mob_name ram and color all are local variables
        self.color = "blue"

    def mob_det(self):  # mob_det is a instance method
        print(
            f'mobile name {self.name} ram is {self.ram} color is {self.color}')


mob = Mobile()  # object creation
mob.mob_det()

print("---------------default constructor-------------")


class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self):
        print("Self address : ", self)
        self.eid = 27
        self.name = "kumar"
        self.sal = 10000

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


emp1 = Employee()
emp1.get_edata()  # Employee.get_edata(emp1)

print("-----------------parameterized constructor-------------------")
""" Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments
"""


class Mobile:

    def __init__(self, name, ram, color):  # default constructor
        self.name = name  # self.name ,self.ram , self.color all are instance variables
        self.ram = ram  # mob_name ram and color all are local variables
        self.color = color

    def mob_det(self):  # mob_det is a instance method
        print(
            f'mobile name {self.name} ram is {self.ram} color is {self.color}')


mob = Mobile('real_me', '6GB', 'gray')  # object creation
mob.mob_det()

print("------------------------Default arguments --------------------")


class Student:
    def __init__(self, name, age, loc="ATP", clg="SKU"):
        self.name = name
        self.age = age
        self.loc = loc
        self.clg = clg

    def stu_data(self):
        print("college name :", self.clg)
        print(
            f'student name is {self.name} age is {self.age} location {self.loc}')


kumar = Student('kumar', 24)
kumar.stu_data()

kiran = Student('kiran', 24, 'hyd')
kiran.stu_data()

yuva = Student('yuva', 24, 'hyd', 'jntuh')
yuva.stu_data()

print("------------default arguments in Employee data------------")


class Employee:
    def __init__(self, name, id, age, com='MCS', loc='banglure'):
        self.name = name
        self.id = id
        self.age = age
        self.com = com
        self.loc = loc

    def emp_data(self):
        print("employee name   :", self.name)
        print("id              :", self.id)
        print("age             :", self.age)
        print("company         :", self.com)
        print("location        :", self.loc)


emp = Employee('kiran', 20, 24)
emp.emp_data()

emp = Employee('kumar', 27, 25, 'TCS', 'hyd')
emp.emp_data()

print("------------keyword arguments in Employee data------------")


class Employee:
    def __init__(self, name='kumar', id=27, com='MCS'):
        self.name = name
        self.id = id
        self.com = com

    def emp_data(self):
        print("employee name   :", self.name)
        print("id              :", self.id)
        print("company         :", self.com)


kiran = Employee(name='kiran', id=28, com='mcs')
kiran.emp_data()
print("----------------------")
kumar = Employee()
kumar.emp_data()
print('--------------------')
yuvi = Employee(id=27, com='TCS', name='yuvi')
yuvi.emp_data()
