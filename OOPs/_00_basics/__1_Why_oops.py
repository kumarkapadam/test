class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)


ali = Student(27, 'kiran',98)
ali.get_sinfo()

print("--------------Product example in OOPs-----------------")


class Product:
    # STATE
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price

    # BEHAVIOR
    def get_pinfo(self):
        print("Product details are : ", self.pid, self.pname, self.price)


tv = Product('SAM001', 'SAMSUNG 32 INC.', 25000)
tv.get_pinfo()

print("****************************      create class  **********************")


class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def stu_det(self):
        print(f'student details is ')
        print(f'student name is :', self.name)
        print(f'student age is :', self.age)
        print(f'student roll number is :', self.roll)


stu1 = Student('kumar', 25, 27)
stu1.stu_det()
