#1.function overriding
# class Employee:
#     def get_designation(self):
#         print("Designation: Employee")
# class Manager(Employee):
#     def get_designation(self):
#         print("Designation: Manager")
# M1 = Manager()
# M1.get_designation()  # Output: Designation: Manager

# 2.duck typing
class Bird:
    def fly(self):
        print("Bird is flying")     
class Airplane:
    def fly(self):
        print("Airplane is flying")

bird = Bird()
airplane = Airplane()               
bird.fly()
airplane.fly()