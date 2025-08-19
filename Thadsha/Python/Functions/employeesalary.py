month=["January","February","March","April","May","June","July","Auguest","Septemper","October","November","December"]
salaries=[40000,50000,70000,100000,120000,150000,170000,200000,210000,250000,300000,310000]
taxes=[]

totalsalary = 0
totaltax = 0
print(f"{'Month':<10} {'Salary':>12} {'Tax':>12} {'Net Salary':>12}")
for i in range(len(salaries)):
    salary = salaries[i]
    months = month[i]
    if 0<salary<50000:
        tax=salary*3/100
    elif 50000<=salary<100000:
        tax=salary*5/100
    elif 100000<=salary<300000:
        tax=salary*8/100
    elif salary>=300000:
        tax=salary*10/100
    taxes.insert(i,tax)

    netsalary=salary-tax
    totalsalary+=netsalary
    totaltax+=tax
    print(f"{month[i]:<10} {salaries[i]:>12} {taxes[i]:>12} {netsalary:>12}")

print(f"\nTotal Net Salary:{totalsalary}")
print(f"Total Tax:{totaltax}")