x=1
while x<=5:
    y=1
    while y<=x:
        print(y,end = ',' if y < x else '')
        y+= 1
    print()
    x+=1