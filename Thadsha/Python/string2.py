# ================================
# PYTHON STRING BUILT-IN FUNCTIONS
# ================================

# String declaration
s = " Welcome to Python "
print(s)   # Print original string

# Convert string to lowercase
print('lower', s.lower())

# Convert string to uppercase
print('upper', s.upper())

# Convert string to title case
print('title', s.title())

# Capitalize first character
print('capitalize', s.capitalize())

# Swap upper to lower and lower to upper
print('swapcase', s.swapcase())

# Check whether string contains only alphabets
print('isalpha', s.isalpha())

# Check whether string contains only digits
print('isdigit', s.isdigit())

# Check whether string is in lowercase
print('islower', s.islower())

# Check whether string is in uppercase
print('isupper', s.isupper())

# Check whether string contains only spaces
print('isspace', s.isspace())

# Check whether string starts with given word
print('startswith', s.startswith('Welcome'))

# Check whether string ends with given character
print('endswith', s.endswith('n'))

# Find position of substring (returns -1 if not found)
print('find', s.find('to'))

# Find position of substring (error if not found)
print('index', s.index('to'))

# Count number of occurrences of a character
print('count', s.count('t'))

# Replace a word in the string
print('replace', s.replace('Python', 'java'))

# Remove spaces from both sides
print('strip', s.strip())

# Remove spaces from left side
print('lstrip', s.lstrip())

# Split string into list
print('split', s.split())

