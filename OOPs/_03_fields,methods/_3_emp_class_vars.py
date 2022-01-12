
print("----Without class variables---------")
class Employee:
    # instance variables - each object has their own data
    # Here problem is comp name is sharable to all employees(objects)
    def __init__(self, eid, name, sal, comp):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.comp = comp

    def get_edata(self):
        print("Employee information :", self.eid, self.name, self.sal, self.comp)

kumar = Employee(1, 'kumar', 10000, 'MCS')
kumar.get_edata()
sai = Employee(2, 'sai', 25000, 'TCS')
sai.get_edata()

print("----With class variables---------")
class Employee:

    comp = 'ORACLE SERVICES'  # class variable, this is sharable to all objects

    def __init__(self, eid, name, sal):  # local variables
        self.eid = eid   # LHS instance variables
        self.name = name
        self.sal = sal

    def get_edata(self):  # instance method
        print("Employee information :", self.eid, self.name, self.sal, Employee.comp) # This is correct
        print("Employee information :", self.eid, self.name, self.sal, self.comp)


veera = Employee(100, 'veerendra', 10000)
veera.get_edata()


santhosh = Employee(101, 'santhosh', 15000)
santhosh.get_edata()
