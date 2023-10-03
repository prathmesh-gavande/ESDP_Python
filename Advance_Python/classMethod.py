class test :
    count=0  # static variable or class object 
    def __init__ (self):
        test.count=test.count+ 1
        
    @classmethod
    def showCountObject(cls): # class method
        print("number of object created : ",cls.count) # cls.count is use to acess class object
        
t1=test()
t2=test()
test.showCountObject()
t3=test()
t4=test()
test.showCountObject()

# method with  parameter (self) known as instance method
# method without  parameter (self) known as static method
