from A import A
class C(A):
    def __init__(self,x,z):
        super().__init__(x)
        self.z = z

    def getz(self):
        print("C:",self.z)