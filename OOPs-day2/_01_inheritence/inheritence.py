# single_inheritance


class Father:  # super class
    def __init__(self):  # default constructor
        self.property = 400000

    def dis_pro(self):  # instance method
        print(f'father property :', self.property)


class Son(Father):  # sub class
    pass


# object creation
s = Son()
s.dis_pro()


class Father:  # super class
    def __init__(self):  # default constructor
        self.property = 400000

    def dis_pro(self):  # instance method
        print(f'father property :', self.property)


class Son(Father):  # sub class
    def __init__(self):  # default constructor
        self.property = 200000

    def dis_pro(self):  # instance method
        print(f'son property :', self.property)


# object creation
s = Son()
s.dis_pro()

print("---------------------single inheritance -------------------")


class Animal:

    def __init__(self):
        print("this is a super class")

    def eating(self):
        print("animal eating ")


class Tiger(Animal):

    def __init__(self):
        print("this is tiger class")

    def sleeping(self):
        print("tiger is sleeping")


print("--------super class object creation--------")
animal = Animal()
animal.eating()
# animal.sleeping()

print("--------sub class object creation--------")
tiger = Tiger()  # Tiger tiger = new Tiger()  int x = 10
tiger.eating()  # inherited super class method
tiger.sleeping()  # sub class specific method


class Parent:  # super class
    def __init__(self, city):
        self.city = city  # local variable city  # instance variable self.city


class Child(Parent):  # sub class
    def __init__(self, name, age, city):
        super().__init__(city)
        self.name = name
        self.age = age

    def display(self):  # instance method
        print(f'this is child class')
        print(f'name is {self.name} age is {self.age} and city is {self.city}')


ob1 = Child('yuvi', 23, 'banglore')  # object creation
ob1.display()


class Person:  # super class
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


class Student(Person):  # sub class
    def __init__(self, fname, lname, age, college):
        super().__init__(fname, lname, age)
        self.college = college

    def display(self):  # instance method
        print(f'this is child class')
        print(f'name is {self.fname} {self.lname} age is {self.age} ')
        print(f'college name is:', self.college)


stu1 = Student('kumar', 'kapadam', 24, 'JNTUH')  # object creation
stu1.display()

stu2 = Student('kiran', 'kapadam', 20, 'adithya')  # object creation
stu2.display()

print("------------using constructor-------------------")


class Family:  # super class
    # Parent class constructor
    def __init__(self, name):
        self.name = name


# Father class inherited from Family
class Father(Family):  # sub class
    # Child class constructor
    def __init__(self, name, age):
        #  Parent class constructor called from child class
        Family.__init__(self, name)
        self.age = age


f = Father("kumar", 26)
print("father name: ", f.name)
print("age        : ", f.age)
