''''print("line1")'''
''''if(True):
    print("line2")
if(False):
    print("line3")
   
is_bool=input("Enter True or False")
    
if is_bool:
    print('line1')
else:
    print('line2')
    
is_integer=input("Enter Your Marks")
y=bool(is_integer)
print(y)


marks=input("Enter Your Marks")
mark=int(marks)
if mark>=75 and mark<=100:
  print('A') 
else: 
    if mark>=65 and mark<=74 :
         print('B')
    else: 
       if mark>=55 and mark<=64:
          print('C')
       else: 
        if mark>=45 and mark<=54:
            print('S')
        else: 
           if mark>0 and mark<=44:
               print('F')
           else:
               print("Enter Your correct marks")
               
               
marks=input("Enter Your Marks")
mark=int(marks)
if mark>=75 and mark<=100:
   print('A') 
elif mark>=65 and mark<=74 :
   print('B')
elif mark>=55 and mark<=64:
   print('C')
elif mark>=45 and mark<=54:
   print('S')
elif mark>0 and mark<=44:
   print('F')
else:
   print("Enter Your correct marks")'''
              
 
minutes=input("Enter Your Minutes")
min=float(minutes)
if min>0 and min<=30:
    print("price=",(min*2))
elif min>=31 and min<=60:
    print("price=",(60+(min-30)*1.50))
elif min>=61 and min<=120:
    print("price=",(95+(min-60)*1))
elif min>=121:
    print("price=",(155+(min-120)*0.50))