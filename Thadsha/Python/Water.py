water = input("Enter the use waterliter: ")
liter = float(water)
bill=3;
bill2=5;
bill3=10;
if liter>0:
    if liter>=0 and liter<=1000 :
        price = 500
    elif liter>=1001 and liter<=3000:
        price = 500 + (liter-1000)*bill
    elif liter>=3001 and liter<=10000:
        price = 500 + 2000*bill + (liter-3000)*bill2
    else:
        price = 500 + 2000*bill +7000*bill2 +(liter-10000)*bill3
    print(f"Price = {price}")
else:
    print(" Enter the correct waterliter ")
    
   