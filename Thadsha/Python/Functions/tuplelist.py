studentscount=int(input("How many students? "))
students=[]

subjectcount=int(input("How many subjects? "))
subjects=[]

for y in range(subjectcount):
    subjectname=input(f"Enter subject name {y + 1}: ")
    subjects.append(subjectname)
    
averagelist = [] 
studentlist=[]

for x in range(studentscount):
    studentname=input(f"\nEnter student name {x + 1}: ")
    marks=[]
    for subject in subjects:
        mark=float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
        
    total=sum(marks)
    average=total/subjectcount
    averagelist.append(average)

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
        
        studentlist.append([studentname]+marks+[total,average,result])
sortaverage=sorted(averagelist,reverse=True)
heading = f"{'Name':<10}"
for subject in subjects:
    heading += f"{subject:>8}"
heading += f"{'Total':>8}{'average':>8}{'result':>8}"
print("\n" + heading)
printedaverages = []

for average in sortaverage:
    for student in studentlist:
        if student[-2] == average:
            list = f"{student[0]:<10}"
            for mark in student[1:1+sub_count]:
                list += f"{mark:>8}"
            list += f"{student[-3]:>8}{student[-2]:>8.2f}{student[-1]:>8}"
            print(list)