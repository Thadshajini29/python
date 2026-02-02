units = input("Enter Your Units: ")
try:
    unit = float(units)
except ValueError:
    print("Please enter a valid number!")
    exit()

if unit > 0:
    if unit <= 90:
        price = unit * 7
    elif unit <= 150:
        price = 90 * 7 + (unit - 90) * 10
    elif unit <= 300:
        price = 90 * 7 + 60 * 10 + (unit - 150) * 15
    else:
        # Units above 300 with 3% surcharge
        base = 90 * 7 + 60 * 10 + 150 * 15 + (unit - 300) * 20
        price = base * 1.03

    print(f"Price = {price:.2f}")
else:
    print("Enter a correct number of units")
