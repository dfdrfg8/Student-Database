class StudentDatabase():
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
    
class Student():
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
    
        StudentDatabase.add_student(self)
    

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print("Student enrolled successfully")
        else:
            print("Student is already enrolled")

    def drop_student(self): 
        if not self.__is_enrolled:
            print("Student is not enrolled")
        else:
            self.__is_enrolled = False
            print("Student has been dropped")


    

    def view_student_info(self): 
        if self.enroll_student:
            status = "Enrolled"
        else:
            status = "Not Enrolled"
        
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {status}")



def menu():
    while True:
        print("\n--- Student Database Menu ---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
    
        choise = input("Enter your choise 1-4: ")

        if choise == "1":
            # Viws All Students
            if not StudentDatabase.student_list:
                print("no student is found")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()
                    print("-" * 30)
        
        
        elif choise == "2":
            #enroll student 
            try:
                sid = int(input("Enter student ID: "))
                student = None
                for s in StudentDatabase.student_list:
                    if s.student_id == sid:
                        student = s
                        break
                if student is None:
                    print("Invalied student id")
                
                else:
                    student.enroll_student()
                
                

            except ValueError:
                print("Please enter valied ID")

        

        elif choise == "3":
            #Drop Student
            try:
                sid = int(input("Enter student ID: "))
                student = None
                for s in StudentDatabase.student_list:
                    if s.student_id == sid:
                        student = s
                        break
                if student is None:
                    print("Invalied student id")
                
                else:
                    student.drop_student()
                
                
            except ValueError:
                print("Please enter valied ID")




        elif choise == "4":
            print("Exiting program. . .")
            break

        else:
            print("Invalied choice. Please enter 1-4")





