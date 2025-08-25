''' = [
    [10, 20, 30],
    [70, 90, 25],
    [40, 98, 26]
]
print(x[0][0])
print(x[1][0])
print(x[1][1])

i=0
while i<3:
    j=0
    while j<3:
        print(x[i][j])
        j+=1
    i+=1'''
    
subjects = ["SFT", "BST", "ICT"]
students = [
    ["Thadsha", [40, 50, 60]],
    ["Kopi", [50, 70, 60]],
    ["Sumi", [60, 70, 30]],
    ["Kavi", [55, 65, 75]],
    ["Aathi", [45, 35, 25]]
]

print(f"{'Student Name':<12} {'BST':<20} {'SFT':<20} {'ICT':<20} {'Total':>6} {'Average':>8} {'Result':>8}")

for student in students:
    name = student[0]
    subjects = student[1]
    total = sum(subjects)
    average = total / len(subjects)

    if 75 <= average <= 100:
        result = 'A'
    elif 65 <= average < 75:
        result = 'B'
    elif 55 <= average < 65:
        result = 'C'
    elif 45 <= average < 55:
        result = 'S'
    elif 0 <= average < 45:
        result = 'F'
    else:
        result="correct Format"


    print(f"{name:<12} {subjects[0]:<20} {subjects[1]:<20} {subjects[2]:<20} {total:>6} {average:>8.2f} {result:>8}")   