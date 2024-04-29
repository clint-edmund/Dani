# Input statements
num_students = int(input("Enter the number of students in the class: "))
passing_grade = float(input("Enter the passing grade: "))

total_average = 0
passed_students = 0

# Loop to collect data for each student
for n in range(num_students):
    name = input("Enter student's name: ")
    average = float(input("Enter student's average grade: "))

    total_average += average

    if average >= passing_grade:
        passed_students += 1

# Calculate class average
class_average = total_average / num_students

# Output results
print("Class Summary:")
print("Total number of students:", num_students)
print("Number of students passed:", passed_students)
print("Class average grade:", class_average)
