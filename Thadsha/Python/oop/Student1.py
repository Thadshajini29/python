class Student1:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print("my name is :"+self.name)
        print("my id is :"+str(self.id))
        
        
Stu1=Student1("Seelan",1000)
Stu1.display()

Stu2=Student1("Thadshajini",22922)
Stu2.display()