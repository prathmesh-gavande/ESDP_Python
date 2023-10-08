class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(A,B,C):
    def showD(self):
       print("Class D")

obj3=D()
obj3.showA()
obj3.showB()
obj3.showC()
obj3.showD()
