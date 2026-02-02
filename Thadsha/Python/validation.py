# num = input("Please enter number")
# while not num.isdigit():
#     print('Please enter correct number')
#     num = input('please enter number')
    
# ---------- First Name Validation ----------
fname = input("Enter Your First Name: ")

# Check if first name contains any digits
while any(x.isdigit() for x in fname):
    print("Correct Your First Name")
    fname = input("Enter Your First Name: ")

print("First name is:", fname)


# ---------- Last Name Validation ----------
lname = input("Enter Your Last Name: ")

# Check if last name contains any digits
while any(y.isdigit() for y in lname):
    print("Correct Your First Name")
    lname = input("Enter Your Last Name: ")

print("Last name is:", lname)


# ---------- Age Validation ----------
age = input("Enter Your age:")

# Allow only numeric age
while not age.isdigit():
    print("Correct Your age")
    age = input("Enter Your age correct format")

print("Your Age:", age)


# ---------- NIC Validation ----------
nic = input("Enter Your NIC Number: ")

# Old NIC format (10 characters)
if len(nic) == 10:
    year = int("19" + nic[:2])     # Extract birth year
    days = int(nic[2:5])           # Extract days

# New NIC format (12 digits)
elif len(nic) == 12 and nic.isdigit():
    year = int(nic[:4])            # Extract birth year
    days = int(nic[4:7])           # Extract days

# Invalid NIC
else:
    print("Invalid NIC")
    exit()


# ---------- Gender Identification ----------
if days > 500:
    gender = "Female"
    days -= 500
else:
    gender = "Male"


# ---------- Date of Birth Calculation ----------
import datetime

# Calculate DOB using year and days
dob_date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=days - 1)

# Format DOB
dob_str = dob_date.strftime("%Y-%m-%d")


# ---------- Age Calculation ----------
today = datetime.date.today()

cal_age = today.year - dob_date.year - (
    (today.month, today.day) < (dob_date.month, dob_date.day)
)


# ---------- Final Output ----------
print("Your Date of Birth:", dob_date.strftime("%d %B %Y"))
print("Your Gender:", gender)
print("Your Age:", cal_age)
