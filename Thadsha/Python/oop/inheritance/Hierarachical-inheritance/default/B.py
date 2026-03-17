from A import A
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20

    def gety(self):
        print("B:",self.y)