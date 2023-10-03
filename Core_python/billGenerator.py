total=50
amt=0
def bill(units):
     if units<=50 :
         amt=units*2.60 
         total=amt+25
         return total
     elif 51<=units<=100:
          amt=(units-50)*3.25
          total =amt+35+(50*2.60)
          return total
     elif 101<=units<=200:
          amt=(units-100)*5.26
          total=amt+45+(50*2.60)+(50*3.25)
          return total
     else:
          amt=(units-200)*8.45
          total=amt+75+(50*2.60)+(50*3.25)+(100*5.26)
          return total
units=int(input("Enter the Units: "))
ans=bill(units)
print (ans)


