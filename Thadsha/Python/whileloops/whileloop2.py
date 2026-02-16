x = 1
while x <= 5:
    y = 1
    while y <= 5:
        if y % 2 == 1:
            print(y, end="")
        else:
            print("*", end="")
        y += 1
        # print()
        x += 1
