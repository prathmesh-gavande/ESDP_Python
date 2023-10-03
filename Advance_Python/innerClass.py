class outer:
    def __init__ (self):
        print("outer class object creation")
    
    class Inner:
        def __init__ (self):
            print("Inner class object creation ")
            
        def fun (self):
            print("This is inner class method ")
            
o=outer()
i=o.Inner()
i.fun()

print("~"*30)

i1=outer().Inner()
i1.fun()
