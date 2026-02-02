# Input number of students and subjects
studentcount = int(input("How many students? "))
subjectcount = int(input("How many subjects? "))

# Input subjects
subjects = []
for i in range(subjectcount):
    subjectname = input(f"Enter your subject {i+1}: ")
    subjects.append(subjectname)

# Input students and marks
studentlist = []
for i in range(studentcount):
    name = input(f"\nEnter the student name {i+1}: ")
    marks = []
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / subjectcount

    # Determine grade
    if average >= 75:
        result = "A"
    elif average >= 65:
        result = "B"
    elif average >= 55:
        result = "C"
    elif average >= 40:
        result = "S"
    else:
        result = "F"

    studentlist.append([name] + marks + [total, average, result])

# Sort students by average (descending)
studentlist.sort(key=lambda x: x[-2], reverse=True)

# Print heading
heading = f"{'Name':<12}"
for subject in subjects:
    heading += f"{subject:>8}"
heading += f"{'Total':>8}{'Average':>8}{'Result':>8}"
print("\n" + heading)
print("-" * len(heading))

# Print each student's data
for student in studentlist:
    row = f"{student[0]:<12}"
    for mark in student[1:1 + subjectcount]:
        row += f"{mark:>8}"
    row += f"{student[-3]:>8}{student[-2]:>8.2f}{student[-1]:>8}"
    print(row)
