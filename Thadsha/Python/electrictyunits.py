units = input("Enter Your Units: ")
unit = float(units)

if unit > 0:
    if unit <= 90:
        price = unit*7
    elif unit <= 150:
        price = 90*7 + (unit-90)*10
    elif unit <= 300:
        price = 90*7 + 60*10 + (unit-150)*15
    else:
        price = (90*7 + 60*10 +150*15 +(unit-300)*15)*1.03
    print(f"Price = {price}")
else:
    print(" Enter Your Correct Units")