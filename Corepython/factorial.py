def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial_recursive(number)}")
