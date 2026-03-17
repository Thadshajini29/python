class A:
    def __init__(self, x):
        self.x = x

    def getx(self):
        print("x:", self.x)


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def gety(self):
        print("y:", self.y)


objB = B(10, 20)
objB.getx()
objB.gety()