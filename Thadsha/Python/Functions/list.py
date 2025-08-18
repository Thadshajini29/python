Subjects=["Maths","English","ICT","History","Science"]
'''print(Subjects)
print(Subjects[0])
print(Subjects[-3])
print(len(Subjects))
x=0
while x<len(Subjects):
    print(Subjects[x])
    print(type(Subjects))
    x+=1
    
y=0
while y<len(Subjects):
    Subjects[y]=input(f"Change Subject {Subjects[y]}{y+1}: ")
    y+=1
print(Subjects)'''

print(Subjects[1:3])
print(Subjects[3:5])
print(Subjects[:3])
print(Subjects[2:])
print(Subjects[::3])