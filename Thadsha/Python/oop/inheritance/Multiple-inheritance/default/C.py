from A import A
from B import B

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.z=30

    def getz(self):
        print("C:",self.z)