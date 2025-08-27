studentcount = int(input("How many students? "))
students = []
subjectcount = int(input("\nHow many subjects?"))
subjects = []
studentlist = []
averagelist = []
for i in range(subjectcount):
    subjectname = input(f"Enter your subject {i+1}: ")
    subjects.append(subjectname)
for i in range(studentcount):
    name = input(f"\nEnter the studentname {i+1}: ")
    marks = []
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    total = sum(marks)
    average = total / len(marks)
    averagelist.append(average)
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
sorted_averages = sorted(averagelist, reverse=True)

heading = f"{'Name':<10}"
for subject in subjects:
    heading += f"{subject:>8}"
heading += f"{'Total':>8}{'average':>8}{'result':>8}"
print("\n" + heading)
printedaverages = []

for average in sorted_averages:
    for student in studentlist:
        if student[-2] == average:
            data = f"{student[0]:<10}"
            for mark in student[1:1+subjectcount]:
                data += f"{mark:>8}"
            data += f"{student[-3]:>8}{student[-2]:>8.2f}{student[-1]:>8}"
            print(data)