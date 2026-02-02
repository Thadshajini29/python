# -------- Function Examples --------

def myname(name):
    print(f"My name is {name}")

myname("Thadshajini")
myname("Sumi")
myname("Kavi")


def getfullname(fname="Thadshajini", lname="Sownthararaja"):
    return f"My full name is {fname} {lname}"

print(getfullname("Thadshajini", "Sownthararaja"))
print(getfullname("Sumi", "Arul"))
print(getfullname())


print("\n" + "=" * 40 + "\n")


# -------- Interest Calculation --------

def calculate(amount, days):
    months = days // 30

    if 3 <= months < 6:
        interest_rate = 12
    elif 6 <= months < 12:
        interest_rate = 12.5
    elif 12 <= months < 36:
        interest_rate = 13
    elif 36 <= months < 60:
        interest_rate = 14
    elif months >= 60:
        interest_rate = 15.5
    else:
        interest_rate = 0

    interest = amount * interest_rate / 100
    total_amount = amount + interest

    print(f"Days        : {days}")
    print(f"Months      : {months}")
    print(f"Rate        : {interest_rate}%")
    print(f"Interest    : {interest:.2f}")
    print(f"Total Amount: {total_amount:.2f}")
    print("-" * 40)


# Function calls
calculate(10000, 90)     # 3 months
calculate(10000, 180)    # 6 months
calculate(10000, 365)    # 12 months
calculate(10000, 1095)   # 36 months
calculate(10000, 1830)   # 60 months
