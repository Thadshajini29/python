'''def myname():
    print("My name is Thadshajini")
myname()

def myname(name):
    print(f"my name is {name}")
    
myname("Thadshajini")
myname("Sumi")
myname("Kavi")

def getfullname(fname,lname):
    print(f"My First name is {fname}")
    print(f"My Last name is {lname}")
    print(f"My full name is {fname}{lname}")
    
getfullname("Thadshajini","Sownthararaja")'''

def getfullname(fname="Thadshajini",lname="Sownthararaja"):
    return(f"My full name is {fname}{lname}")

'''getfullname("Thadshajini","Sownthararaja")
getfullname("Sumi","Arul")
getfullname()'''

myfullname=getfullname()
print(myfullname)
