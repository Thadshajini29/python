studentscount = int(input("How many students? "))
subjectcount = int(input("How many subjects? "))

# Subject input
subjects = []
for y in range(subjectcount):
    subjectname = input(f"Enter subject name {y + 1}: ")
    subjects.append(subjectname)

studentlist = []

# Student input
for x in range(studentscount):
    studentname = input(f"\nEnter student name {x + 1}: ")
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / subjectcount

    # Grade
    if 75 <= average <= 100:
        result = "A"
    elif 65 <= average < 75:
        result = "B"
    elif 55 <= average < 65:
        result = "C"
    elif 45 <= average < 55:
        result = "S"
    else:
        result = "F"

    # Pass / Fail
    if average >= 45:
        status = "PASS"
    else:
        status = "FAIL"

    studentlist.append([studentname] + marks + [total, average, result, status])

# Sort by average (highest first)
studentlist.sort(key=lambda x: x[-3], reverse=True)

# Print heading
heading = f"{'Name':<10}"
for subject in subjects:
    heading += f"{subject:>8}"
heading += f"{'Total':>8}{'Average':>8}{'Grade':>8}{'Status':>10}"
print("\n" + heading)

# Print student data
for student in studentlist:
    row = f"{student[0]:<10}"
    for mark in student[1:1 + subjectcount]:
        row += f"{mark:>8.1f}"
    row += f"{student[-4]:>8.1f}{student[-3]:>8.2f}{student[-2]:>8}{student[-1]:>10}"
    print(row)
