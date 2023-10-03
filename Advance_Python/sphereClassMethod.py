class sphere :

    def sur_area(self,radius):
        area=4*3.14*radius*radius
        print("Surface area of sphere : ",area)

    def vol(self,radius):
        volume=(4*3.14*radius*radius*radius)/3
        print("Volume of Sphere : ",volume)

s1=sphere()
s1.sur_area(4)
s1.vol(4)

        

