month = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

salaries = [
    40000, 50000, 70000, 100000, 120000, 150000,
    170000, 200000, 210000, 250000, 300000, 310000
]

taxes = []

total_net_salary = 0
total_tax = 0
total_gross_salary = 0

print(f"{'Month':<12}{'Salary':>15}{'Tax %':>10}{'Tax':>15}{'Net Salary':>15}")
print("-" * 67)

for i in range(len(salaries)):
    salary = salaries[i]
    month_name = month[i]

    if salary < 50000:
        tax_rate = 3
    elif salary < 100000:
        tax_rate = 5
    elif salary < 300000:
        tax_rate = 8
    else:
        tax_rate = 10

    tax = salary * tax_rate / 100
    taxes.append(tax)

    net_salary = salary - tax

    total_gross_salary += salary
    total_net_salary += net_salary
    total_tax += tax

    print(
        f"{month_name:<12}"
        f"{salary:>15,.2f}"
        f"{tax_rate:>10}%"
        f"{tax:>15,.2f}"
        f"{net_salary:>15,.2f}"
    )

print("-" * 67)

# Annual Summary
print("ANNUAL SUMMARY")
print("-" * 67)
print(f"{'Total Gross Salary':<25}{total_gross_salary:>42,.2f}")
print(f"{'Total Tax Paid':<25}{total_tax:>42,.2f}")
print(f"{'Total Net Salary':<25}{total_net_salary:>42,.2f}")

average_monthly_salary = total_gross_salary / len(salaries)
average_monthly_tax = total_tax / len(salaries)

print(f"{'Average Monthly Salary':<25}{average_monthly_salary:>42,.2f}")
print(f"{'Average Monthly Tax':<25}{average_monthly_tax:>42,.2f}")
