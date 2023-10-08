            
# single level inheritance  
class A:
    def showA(self):
        print("class A")
        
class B(A):
    def showB(self):
        print("Class B")
        
obj=B()
obj.showA()
obj.showB()
