from B import B

class C(B):
    def __init__(self):
        super().__init__()
        self.z=30

    def getz(self):
        print("C:",self.z)