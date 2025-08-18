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
    if days==90:
        interest = amount*12/100
    elif days==180:
        interest = amount*12.5/100
    elif days==365:
        interest = amount*13/100
    elif days==1095:
        interest = amount*14/100
    else:
        interest = amount*15.5/100

    total_amount = amount+interest
    print("interest",interest)
    print("Total amount:",total_amount)

calculate(10000,90)
calculate(10000,180)
calculate(10000,365)
calculate(10000,1095)
calculate(10000,1830)    