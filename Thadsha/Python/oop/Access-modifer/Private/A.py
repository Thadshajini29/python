class A:
    def __init__(self):
        self.__x =10 # using double underscore to make it private

    def getx(self):
        print("A:",self.__x) #access private modifier using public method