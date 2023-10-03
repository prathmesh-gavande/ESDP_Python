
subject1_marks = float(input("Enter marks for subject 1: "))
subject2_marks = float(input("Enter marks for subject 2: "))
subject3_marks = float(input("Enter marks for subject 3: "))
subject4_marks = float(input("Enter marks for subject 4: "))

total_possible_marks = float(input("Enter the total possible marks: "))

total_marks = subject1_marks + subject2_marks + subject3_marks + subject4_marks

percentage = (total_marks / total_possible_marks) * 100

print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
