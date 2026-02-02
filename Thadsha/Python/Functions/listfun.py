# ---------- SUBJECT LIST ----------
subject = ["Maths", "Tamil", "English"]

# Add items
subject.append("ICT")
print("After append:", subject)

subject.insert(2, "SFT")
print("After insert:", subject)

subject.extend(["BST", "ET"])
print("After extend:", subject)

# Remove items
subject.pop(2)
print("After pop index 2:", subject)

subject.pop()
print("After pop last:", subject)

subject.remove("Tamil")
print("After remove Tamil:", subject)

# Conditional remove
if "ICT" in subject:
    subject.remove("ICT")
    print("After removing ICT:", subject)

# Index
print("Index of English:", subject.index("English"))

# Sorting
subject.sort()
print("Sorted:", subject)

subject.reverse()
print("Reversed:", subject)

subject.sort(reverse=True)
print("Sorted descending:", subject)


print("\n-----------------------------\n")


# ---------- MARKS LIST ----------
marks = [70, 80, 40, 50, 60, 90]

print("Marks:", marks)
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))

# Copy list
marksD = marks.copy()
print("Copied marks:", marksD)

# Modify copied list
marksD.append(85)
print("After appending to copy:", marksD)
print("Original marks (unchanged):", marks)
