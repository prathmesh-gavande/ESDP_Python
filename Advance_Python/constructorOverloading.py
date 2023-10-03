class test:
    def __init__ (self,a=None,b=None,c=None):
        print("constructor with variable arguments",a ,b,c,)
        
t=test()
t=test(10)
t=test(10,20)
t=test(10,20,30)

