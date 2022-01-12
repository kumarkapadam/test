"""# how to create a class and its objects

class Student:
    name = 'kumar'
    age =20

stu1 = Student()
print("name is",stu1.name)
print("age is ",stu1.age)


# How to create a Class using type in Python?

e1 = type('Employee',() ,{})()
print(e1)


e1.name ='kumar'
print(e1.name)


#How to create data attributes of a class in run-time in python?


class Student:
    pass

stu1 = Student()
setattr(stu1,'salary',20000)

stu2 = Student()
setattr(stu2,'salary',200)

print(stu1.salary)
print(stu2.salary)


#How to use self parameter to maintain state of object in Python?

class State:
    def __init__(self):
        self.x = 10.0
    def add(self,y):
        self.x+=y
    def sub(self,y):
        self.x-=y
    def mul(self,y):
        self.x*=y

s =State()
print(s.x)
s.add(10)
print(s.x)



class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for num in Counter(5, 15):
    print(num)




class Student:
    def __init__(self):
        self.name = "kumar"
        self.age = 25
        self.course = 'python'

stu1 = Student()
temp = vars(Student)
for item in temp:
    print(item ,"----",temp[item])  """

#How to copy all properties of an object to another object in Python?

class Student:
    def __init__(self):
        self.name = 'kumar'
        self.age =24

stu = Student()
print(stu.name)
print(stu.age)

stu1 = Student()
stu.__dict__.update(stu1.__dict__)

print(stu1.__dict__)
print(stu1.name,stu1.age)


temp = vars(stu1)
for item in temp:
    print(item,"---",temp[item])



















