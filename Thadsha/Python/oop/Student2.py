class Student2:
    
    def __init__(self,fname,lname,id):
        self.fname=fname
        self.id=id
        self.lname=lname
        
    def getfullname(self):
        return self.fname+self.lname
        
    def display(self):
        print("my fullname is :"+self.getfullname())
        print("my id is :"+str(self.id))
        
        
Stu2=Student2("Seelan","Yoga",1000)
Stu2.display()