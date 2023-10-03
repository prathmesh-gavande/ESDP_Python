class Employee:
    def __init__ (self,no,name,sal):
        self.eno=no
        self.ename=name
        self.esal=sal
        
    def showdetails (self):
        print("Employee no. ",self.eno)
        print("Employee name ",self.ename)
        print("Employee sallary ",self.esal)
        
class test:
    def updates(Employee):
        Employee.esal=Employee.esal+8000
        Employee.showdetails()
        
e=Employee(9,"Prathmesh",20000)
e.showdetails()
test.updates(e)
