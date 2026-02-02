print("==== Water Bill Calculation ====")

water = input("Enter the used water in liters: ")
try:
    liter = float(water)
except ValueError:
    print("Please enter a valid number!")
    exit()

bill = 3   # Rate for 1001–3000 liters
bill2 = 5  # Rate for 3001–10000 liters
bill3 = 10 # Rate for >10000 liters

if liter > 0:
    if liter <= 1000:
        price = 500
    elif liter <= 3000:
        price = 500 + (liter - 1000) * bill
    elif liter <= 10000:
        price = 500 + 2000 * bill + (liter - 3000) * bill2
    else:
        price = 500 + 2000 * bill + 7000 * bill2 + (liter - 10000) * bill3
    
    print(f"Price = {price:.2f}")
else:
    print("Enter the correct water liter")
