'''
Instance variables
Instance methods
'''

def func1():
    print("Function body")

func1()




class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


madhu = Employee(100, 'kumar', 10000)
madhu.get_edata()

