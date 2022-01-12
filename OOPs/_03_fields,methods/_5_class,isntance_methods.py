class Employee:
    company_name = "modernize chip solutions pvt limited"

    def __init__(self, emp_name, emp_age):
        self.emp_name = emp_name
        self.emp_age = emp_age

    def emp_details(self):
        print("------------employee detials---------------")
        print(
            f"employee name {self.emp_name} and employee age is {self.emp_age}")


emp1 = Employee("kumar", 24)
emp1.emp_details()

print(emp1.company_name)
print(emp1.__dict__)




class Employee:
    raise_amount = 2.0
    number_of_employees = 0

    def __init__(self, first, last, age, salary):
        self.first = first
        self.last = last
        self.age = age
        self.salary = salary
        self.gmail = first + '-' + last + "@gmail.com"
        Employee.number_of_employees += 1

    def emp_full_name(self):
        print(f"employee full name is {self.first} {self.last}")

    def emp_details(self):
        print("-----employee details------------")
        print(
            f"employee name is {emp.emp_full_name()} self.age {self.age} salary is{self.salary}")

    def raise_salary(self):
        return self.salary * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp = Employee('kumar', 'kapadam', 24, 20000)
emp1 = Employee('kum', 'kk', 23, 15000)
emp.emp_details()
print(emp.salary)
print("---------after raising----------")
print(emp.raise_salary())
print(Employee.number_of_employees)

print(Employee.set_raise_amt(3))

print(emp.salary)
print("---------after raising----------")
print(emp.raise_salary())
print(Employee.number_of_employees)





class Car:
    base_price = 10000  # class variable

    def __init__(self, windows, doors, power):  # constructor with parameters
        self.windows = windows  # local variables : windows,doors,power
        self.doors = doors  # instance variable : self.windows ,self.doors , self.power
        self.power = power

    def display(self):   # instance method
        print("--------car details---------")
        print(f"{self.windows} {self.doors} {self.power}")

    @classmethod
    def increment(cls, incre):  # class method
        cls.base_price = cls.base_price + cls.base_price * incre


car1 = Car(4, 6, 2000)  # object creation
car1.display()
print(car1.base_price)
car1.increment(10)
print(car1.base_price)



