class Student:
    
    def __init__ (self):
        self.name=""
        self.roll=1
        self.Add=" Enter the address"
        self.per=int(0.0)
        
    def datainput(self):
        self.name=input("Enter the name: ")
        self.roll=input("Enter the roll number: ")
        self.add=input("Enter the address: ")
        self.per=input("Enter the percentages: ")
        
    def display(self):
        print("Name : ",self.name)
        print("roll No . : ",self.roll)
        print("Address : ",self.Add)
        print("percentages : ",self.per)
        
        if self.per >= 70:
            print("You are in Distinction")
        elif self.per >= 60 and self.per < 70:
            print("you are in first class")
        elif self.per >= 40 and self.per < 60:
            print("You are in second class")
        else:
            print("you are fail")
        
s1=Student()
s1.datainput()
s1.display()
