# #multilevel inheritance
# class Employee:
#     start_time = "10am"
#     end_time = "5pm"
# class Adminstaff(Employee):
#     def __init__(self,role):
#         self.role= role
# class Accountant(Adminstaff):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary = salary 
# acc1 = Accountant(80000,"CA")   
# print(acc1.role , acc1.salary , acc1.start_time)    
#multiple inheritance
class teacher:
    def __init__(self,salary):
       self.salary = salary
class student:
    def __init__(self,gpa):
        self.gpa = gpa
class TA(teacher,student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)  
        student.__init__(self,gpa)
        self.name =name
ta1 = TA(150000,9.7,"vanshi")    
print(ta1.salary ,ta1.name,ta1.gpa)    
             

    