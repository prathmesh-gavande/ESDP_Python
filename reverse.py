num=int(input("Enter the number :"))
print(num)
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

#num = 123456
#print(str(num)[::-1])