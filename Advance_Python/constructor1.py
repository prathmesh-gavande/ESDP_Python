class Electricity:

    def __init__(self,name,unit) :
        self.name=name
        self.unit=unit
        
    
    def Bill(self):
        
        if(self.unit<30):
            print("Name : ",self.name)
            print("Electric Bill : ",self.unit*1.5)
        elif(self.unit <200):
            print("Name : ",self.name)
            print("Electric Bill : ",self.unit*3)
        else:
            print("Name : ",self.name)
            print("Electric Bill : ",self.unit*4.25)

cus1=Electricity("Prathmesh",90)
cus1.Bill()


    
