# ================================
# STRING HANDLING & DOB DIGIT SUM
# ================================

# String declaration
x = "Welcome to Python"

# Print string and basic properties
print(x)                 # Print full string
print(len(x))            # Length of the string
print(x[0])              # First character
print(x[-4])             # 4th character from last

print("\n********")

# Print string characters using while loop (forward)
i = 0
while i < len(x):
    print(x[i])
    i += 1

print("\n********")

# Print string characters using while loop (reverse)
y = len(x) - 1
while y >= 0:
    print(x[y])
    y -= 1

print("\n********")

# -------------------------------
# DATE OF BIRTH DIGIT SUM
# -------------------------------

# Get date of birth from user
y = input("Enter Your Date of Birth (yyyy.mm.dd): ")
print(y)

# Calculate total of digits
total = 0
for ch in y:
    if ch.isdigit():          # Check only digits
        total += int(ch)

# Reduce total to single digit
while total >= 10:
    x = 0
    for ch in str(total):
        x += int(ch)
    total = x

# Print final result
print(total)

