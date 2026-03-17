class A:
    def __init__(self):
        self.x = 10

    def getx(self):
        print(self.x)


class B(A):
    def __init__(self):
        super().__init__()

    def gety(self):
        print("class A:", self.x)


objB = B()
objB.getx()
objB.gety()