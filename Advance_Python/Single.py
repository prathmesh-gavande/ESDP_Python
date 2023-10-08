class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

obj1=A()
obj1.showA()

obj2=B()
obj2.showA()
obj2.showB()

