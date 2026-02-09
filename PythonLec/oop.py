class Student:
    def __init__(self):
          print("obj has been constructed") #ye galat hai 1 class k andar 1 hi init method hoga varna end vala call hojayga
    def __init__(self,name,cgpa): # parameterized constructor
            self.name= name
            self.cgpa=cgpa
stu1= Student("Urvashi",9.8)
stu2= Student("Vanshi",8.5)
stu3= Student("Kaishka",8.9)
print(stu1.name,"\n",stu1.cgpa)
print(stu3.name)
print(stu2.cgpa)   
     
