students = {}
while True:
    print("Menu")
    print("A. Add Student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E.Exit")

    choice = input("Enter your choice")

    if(choice=="A"):
         name = input("Enter student name: ")
         marks = int(input("Enter marks: "))
         students[name] = marks
         print("Student added successfully.")
    elif(choice=="B"):
        na = input("Enter the name of student you want to update marks")
        if na in students:
            marks = int(input("enter updated marks: "))
            students[na] = marks
            print("marks updated successfully.")
        else: 
            print("student not found")  

    elif choice =="C":
        name = input("enter student name")
        if name in students:
            print(f"{name}'s marks: {students[name]}")  
        else:
            print("Students not found.")
    elif choice =="D":
        if students:
            print("student recods\n")
            for name,marks in students.items():
                print(name,":",marks)
        else:
            print("no records found")
    elif choice == "E":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")

