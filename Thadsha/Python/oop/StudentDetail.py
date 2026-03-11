
class StudentDetail:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def setmarks(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def calctotal(self):
        total=self.marks1+self.marks2+self.marks3
        return total

    def calcaverage(self, total):
        average=total/3
        return average

    def getgrade(self,average):
        if average>=75:
            return"A"
        elif average>=65:
            return"B"
        elif average>=55:
            return"C"
        elif average>=45:
            return"S"
        else:
            return"F"

    def display(self):
        
        total = self.calctotal()
        average = self.calcaverage(total)
        grade = self.getgrade(average)
       
        print("Student Name:"+self.name)
        print("Student ID:"+str(self.id))
        print("Marks1:"+ str(self.marks1))
        print("Marks2:"+ str(self.marks2))
        print("Marks3:"+str(self.marks3))
        print("Total:" +str( total))
        print("Average:"+ str(average))
        print("Grade:"+grade)
        

stu1 = StudentDetail("Thadsha", 101)
stu1.setmarks(50,60,80)
stu1.display()