'''x="Welcome to Python"
print(x)
print(len(x))
print(x[0])
print(x[-4])

print("\n********")

i=0
while i<len(x):
    print(x[i])
    i+=1
    
print("\n********")

y=len(x)-1
while y>=0:
    print(x[y])
    y-=1

print("\n********")

t=abs(len(x))
while (t<=-1):
    print(x[t])
    t=t+1'''
    
'''for i in x:
    print(i)
    
for i in range(0,len(x),1):
    print(x[i])
    
print("\n********")

for i in reversed(x):
    print(i)

a=x[8:10]
print(a)

a=x[-17:-10]
print(a)'''

y=input("Enter Your Date of Birth(yyyy.mm.dd):")
print(y)
total=0
for ch in y:
    if ch.isdigit():
        total+=int(ch)
while total>10:
    x=0
    for ch in str(total):
        x+=int(ch)
    total=x
print(total)