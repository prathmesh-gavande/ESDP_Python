value=int(input("enter the range of series: "))

def fibo(a,b,value):
    if value == 0 :
        return 
    print (a," ")
    value=value-1
    fibo(b , a+b ,value)

fibo (1,1,value)
