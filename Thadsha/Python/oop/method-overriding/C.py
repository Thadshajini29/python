from B import B
class C(B):
    def __init__(self):
        super().__init__()
        self.z=30

    def show(self):
        super().show()
        print("C:",self.z)