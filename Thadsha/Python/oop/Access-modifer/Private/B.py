from A import A


class B(A):
    # constructor of class B
    def __init__(self):
        super().__init__()
        self.y = 20

    # method to access private modifier of class A
    def gety(self):
        print("B:", self.y)

    # method to access private modifier of class A using public method of class A
    def show(self):
        self.getx()
