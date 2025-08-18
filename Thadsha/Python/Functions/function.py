'''def myname():
    print("My name is Thadshajini")
myname()

def myname(name):
    print(f"my name is {name}")
    
myname("Thadshajini")
myname("Sumi")
myname("Kavi")

def getfullname(fname,lname):
    print(f"My First name is {fname}")
    print(f"My Last name is {lname}")
    print(f"My full name is {fname}{lname}")
    
getfullname("Thadshajini","Sownthararaja")

def getfullname(fname="Thadshajini",lname="Sownthararaja"):
    return(f"My full name is {fname}{lname}")

getfullname("Thadshajini","Sownthararaja")
getfullname("Sumi","Arul")
getfullname()

myfullname=getfullname()
print(myfullname'''


def calculate(amount,days):
    month = days // 30

    if month == 3:
        interest_rate = 12
    elif month == 6:
        interest_rate = 12.5
    elif month == 12:
        interest_rate = 13
    elif month == 36:
        interest_rate = 14
    elif month >= 60:
        interest_rate = 15.5
    else:
        interest_rate = 0

    interest = amount * interest_rate / 100
    total_amount = amount + interest

    print("Interest:", interest)
    print("Total amount:", total_amount)
    print("-" * 30)


calculate(10000, 90)
calculate(10000, 180)
calculate(10000, 365)
calculate(10000, 1095)
calculate(10000, 1830)    