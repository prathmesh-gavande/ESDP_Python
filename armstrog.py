number = int(input("Enter a number: "))

num_str = str(number)

num_digits = len(num_str)

sum_of_digits = 0

for digit_char in num_str:
    digit = int(digit_char)
    sum_of_digits += digit ** num_digits

if number == sum_of_digits:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
