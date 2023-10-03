class Timeclass:

    def __init__(self,hr,min):
        self.hr=hr
        self.min=min

     
    def Time(self):
        print("Hour : " ,self.hr)
        print("Minute : ",self.min)

class Dateclass:
    def Date(self):
        print("Today's date")
    
class Studenclass:
    def Student(self):
        print("I am a student")

class Fanclass:
    def Fan(self):
        print("I am rotate")

class Pointclass:
    def Point (self):
        print("Point function")

class Boxclass:
    def Box (self):
        print("Box function")

time1=Timeclass(10,35)
time1.Time()

print("-"*30)
date1=Dateclass()
date1.Date()

