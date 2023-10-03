n = int(input("Enter the value of n: "))

even_sum = 0
count = 0
current_number = 2 

while count < n:
    even_sum += current_number
    current_number += 2  
    count += 1

print(f"The sum of the first {n} even numbers is: {even_sum}")
