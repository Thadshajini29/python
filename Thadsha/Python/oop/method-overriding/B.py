from A import A

class B(A):
    def __init__(self):
        super().__init__()
        self.y=40

    def show(self):
        super().show()
        print("B:",self.y)