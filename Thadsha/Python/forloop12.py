for x in range(1, 5):
    for y in range(1, 6):
        if y % 2 == 1:
            print(y, end='')
        else:
            print("*", end='')
    print()
