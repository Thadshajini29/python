# Initial list of subjects
# Subjects = ["Maths", "English", "ICT", "History", "Science"]

# print("Subjects List:", Subjects)
# print("First Subject:", Subjects[0])
# print("Third from Last Subject:", Subjects[-3])
# print("Total number of subjects:", len(Subjects))

# # Loop to print all subjects with type
# x = 0
# while x < len(Subjects):
#     print(f"Subject {x+1}: {Subjects[x]}, Type: {type(Subjects[x])}")
#     x += 1

# # Loop to change subject names via input
# y = 0
# while y < len(Subjects):
#     Subjects[y] = input(f"Change Subject {y+1} ({Subjects[y]}): ")
#     y += 1

# print("\nUpdated Subjects List:", Subjects)

# # Slicing examples
# print("Subjects[1:3]  ->", Subjects[1:3])
# print("Subjects[3:5]  ->", Subjects[3:5])
# print("Subjects[:3]   ->", Subjects[:3])
# print("Subjects[2:]   ->", Subjects[2:])
# print("Subjects[::3]  ->", Subjects[::3])


    
salaries = [40000,50000,70000,100000,120000,150000,170000,200000,210000,250000,300000,310000]
month = ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]

totalsalary = 0
totaltax = 0

for i in range(len(salaries)):
    salary = salaries[i]
    month_name = month[i]

    if 0 < salary < 50000:
        tax = salary * 3 / 100
    elif salary < 100000:
        tax = salary * 5 / 100
    elif salary < 300000:
        tax = salary * 8 / 100
    elif salary >= 300000:
        tax = salary * 10 / 100
    else:
        tax = 0

    netsalary = salary - tax
    totalsalary += netsalary
    totaltax += tax

    print(f"Month:{month_name}, Salary:{salary}, Tax:{tax}, Net Salary:{netsalary}")

print(f"\nTotal Net Salary:{totalsalary}")
print(f"Total Tax:{totaltax}")


