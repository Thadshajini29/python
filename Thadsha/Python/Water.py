water = input("Enter the use waterliter: ")
liter = float(water)
if liter>0:
    if liter>=0 and liter<=1000 :
        price = 500
    elif liter>=1001 and liter<=3000:
        price = 500 + (liter-1000)*3
    elif liter>=3001 and liter<=10000:
        price = 500 + 2000*3 + (liter-3000)*5
    else:
        price = 500 + 2000*3 +7000*5 +(liter-10000)*10
    print(f"Price = {price}")
else:
    print(" Enter the correct waterliter ")
    
   