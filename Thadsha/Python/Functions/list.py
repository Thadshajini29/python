'''Subjects=["Maths","English","ICT","History","Science"]
print(Subjects)
print(Subjects[0])
print(Subjects[-3])
print(len(Subjects))
x=0
while x<len(Subjects):
    print(Subjects[x])
    print(type(Subjects))
    x+=1
    
y=0
while y<len(Subjects):
    Subjects[y]=input(f"Change Subject {Subjects[y]}{y+1}: ")
    y+=1
print(Subjects)

print(Subjects[1:3])
print(Subjects[3:5])
print(Subjects[:3])
print(Subjects[2:])
print(Subjects[::3])'''

    
salaries=[40000,50000,70000,100000,120000,150000,170000,200000,210000,250000,300000,310000]
month=["January","February","March","April","May","June","July","Auguest","Septemper","October","November","December"]
totalsalary = 0
totaltax = 0
for salary in salaries:
    if salary<50000 and salary>0:
        tax=salary*3/100
    elif salary<100000 and salary>=50000:
        tax=salary*5/100
    elif salary<300000 and salary>=100000:
        tax=salary*8/100
    elif salary>=300000:
        tax=salary*10/100
    else:
        ("correct format")

    netsalary=salary-tax
    totalsalary+=netsalary
    totaltax+=tax
    print(f"Salary:{salary},month:{month},Tax:{tax},Net Salary:{netsalary}")

print(f"\nTotal Net Salary:{totalsalary}")
print(f"Total Tax:{totaltax}")