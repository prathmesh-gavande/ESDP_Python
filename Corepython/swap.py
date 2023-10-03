#Swapping with without using third variable

num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))

print(f"Numbers before swapping:\nnum1: {num1} num2: {num2}")

num1=num1+num2
num2=num1-num2
num1=num1-num2

print(f"Numbers after swapping:\nnum1: {num1} num2: {num2}")