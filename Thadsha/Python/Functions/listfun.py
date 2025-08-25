'''subject=["Maths","Tamil","English"]
subject.append("ICT")
print(subject)
subject.insert(2,"SFT")
print(subject)
subject.extend(["BST","ET"])
print(subject)
subject.pop(2)
print(subject)
subject.pop()
print(subject)
subject.remove("Tamil")
print(subject)
if "ICT" in subject:
    subject.remove("ICT")
    print(subject)
#subject.clear()
print(subject)
print(subject.index("English"))
subject.sort()
print(subject)
subject.reverse()
print(subject)
subject.sort(reverse=True)
print(subject)'''

marks=[70,80,40,50,60,90]
print(max(marks))
print(min(marks))
print(sum(marks))

marksD=[70,80,40,50,60,90]
marksD=marks.copy()
print(marksD)
marksD.append(85)
print(marksD)
print(marks)