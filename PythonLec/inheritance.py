class Employee:
    start_time = "10pm"
    end_time = "6pm"

    def change_time(self,new_endtime):
        self.end_time = new_endtime

class Teacher(Employee): #inhertance
    def __init__(self,name,subject):
        self.subject = subject
        self.name = name

t1 = Teacher("vanshi","maths")        
print(t1.name , t1.subject,t1.start_time , t1.end_time)        

t1.change_time("5pm")
print(t1.end_time)
