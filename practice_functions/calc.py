"""def add():
    assert sum([2,3]) == 10


if __name__ == "__main__":
    add()
    print("test cases is passed")



class Student:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print("student name is :",self.name , "age is :",self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.ram ="4gg"
            self.con = "i5"
        def show(self):
            print("computer configuration is :",self.con , "ram is :",self.ram)


        class config:
            def show(self):
                print("this is the configuration of the system")


stu1 = Student('kumar',25)
stu1.show()





class A:
    def featureA(self):
        print("this is A class")

class B(A):
    def featureB(self):
        print("this is B class")


a=A()
a.featureA()

b = B()
b.featureA()
b.featureB()


class Father:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def father_det(self):
        print("farher details is ",self.name , self.age )

class Son(Father):
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def son_det(self):
        print("son details is :",self.age , self.name)


f1 = Father('kullayappa',51)
f1.father_det()


s1 = Son('kumar',24)
s1.son_det()
s1.father_det()

"""



class Father:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def father_det(self):
        print("farher details is ",self.name , self.age )

class Son(Father):
    def __init__(self,name,age):
        Father.__init__(name,age)
    def son_det(self):
        print("son details is :",self.age , self.name)


f1 = Father('kullayappa',51)
f1.father_det()


s1 =Son('kullayappa',51)
s1.son_det()