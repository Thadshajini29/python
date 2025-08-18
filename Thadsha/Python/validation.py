'''num=input("Please enter number")
while not num.isdigit():
    print('Please enter correct number')
    num=input('please enter number')'''
    
fname=input("Enter Your First Name: ")
while any(x.isdigit()for x in fname):
    print("Correct Your First Name")
    fname=input("Enter Your First Name: ")
print("first name is:",fname)

lname=input("Enter Your Last Name: ")
while any(y.isdigit()for y in lname):
    print("Correct Your First Name")
    lname=input("Enter Your Last Name: ")
print("Last name is:",lname)

age=input("Enter Your age:")
while not age.isdigit():
    print("Correct Your age")
    age=input('Enter Your age correct format')
print("Your Age:",age)

nic=input("Enter Your NIC Number: ")
if len(nic)==10:
    year=int("19" + nic[:2])
    days=int(nic[2:5])
elif len(nic)==12 and nic.isdigit():
    year=int(nic[:4])
    days=int(nic[4:7])
else:
    print("Invalid NIC ")
    exit()
if days>500:
    gender="Female"
    days-=500
else:
    gender="Male"
    
import datetime
dob_date=datetime.datetime(year, 1, 1)+datetime.timedelta(days=days - 1)
dob_str=dob_date.strftime("%Y-%m-%d")

today = datetime.date.today()
cal_age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
   
print("Your Date of Birth:",dob_date.strftime("%d %B %Y"))
print("Your Gender:", gender)
print("Your Age:", cal_age)