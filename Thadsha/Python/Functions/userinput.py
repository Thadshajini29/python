studentscount=int(input("How many students? "))
students=[]

subjectcount=int(input("How many subjects? "))
subjects=[]

for y in range(subjectcount):
    subjectname=input(f"Enter subject name {y + 1}: ")
    subjects.append(subjectname)

for x in range(studentscount):
    studentname=input(f"\nEnter student name {x + 1}: ")
    marks=[]
    for subject in subjects:
        mark=float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
 
    total=sum(marks)
    average=total/subjectcount

    if 75<=average<=100:
        result='A'
    elif 65<=average<75:
        result='B'
    elif 55<=average<65:
        result='C'
    elif 45<=average<55:
        result='S'
    elif 0<=average< 45:
        result='F'
    else:
        result="correct format"

    students.append({
        'name': studentname,
        'marks': marks,
        'total': total,
        'average': average,
        'result': result
    })


print("\nFinal Results:\n")
heading=f"{'Name':<12}"+"".join(f"{subject:<20}" for subject in subjects)+f"{'Total':>8} {'Average':>8} {'Grade':>8}"
print(heading)
print("-" * len(heading))


for student in students:
    line=f"{student['name']:<12}"
    for mark in student['marks']:
        line+=f"{mark:<20}"
    line+=f"{student['total']:>8.2f} {student['average']:>8.2f} {student['result']:>8}"
    print(line)