class student:
    def setName(self,name):
        self.name=name
        
    def getName (self):
        return self.name
        
    def setpercentage(self,percentage):
        self.percentage=percentage
        
    def getPercentage(self):
        return self.percentage
        
n=int(input("Enter the number of students :"))
s=student()

for i in range (n):
    name=input("Enter the student name : ")
    s.setName(name)
    percentage=int(input("Enter the student percentage : "))
    s.setpercentage(percentage)
    print("Hi ",s.getName()," Your Percentage are : ",s.getPercentage())
