# Tuple example
t = (10, 30, 50, 60, 70)
print(t)
print(type(t))
print(t[2])

# List example
marks = [40, 50, 60]
print(marks)

# List inside parentheses (still a list)
t1 = ([40, 50, 60])
print(t1)
print(type(t1))

# Convert list to tuple
tt = tuple(marks)
print(type(tt))

# Tuple concatenation
marks1 = (40, 50, 60)
marks2 = (40, 50, 60)
marks3 = (40, 50, 60)
marks4 = marks1 + marks2 + marks3
print(marks4)

# Tuple unpacking
student = ("Thadshajini", 19, "29/11/2005")
fname, age, dob = student
print(fname)
print(age)
print(dob)

# Extended unpacking
marks = (70, 85, 55, 96)
a, *b, c = marks
print(a)
print(b)
print(c)
