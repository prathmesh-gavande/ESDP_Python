input_string = input("Enter a string: ")

input_string = input_string.replace(" ", "").lower()

reverse_string = input_string[::-1]

if input_string == reverse_string:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
