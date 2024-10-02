class Student:
    def __init__(self, name = None, num = None, curso = None):
        self.name = name
        self.num = num
        self.curso = curso

    def welcomeMessage(self):
        print(f"Welcome {self.name} number {self.num} of course {self.curso} to IADE!")
        
    def inputStudent(self):
        self.name = input("What's your name: ")
        self.num = input("What's your student number: ")
        self.curso = input("What's your course: ")    

    def inputGrades(self):
        grades = []
        print("Please enter your grades (-1 to exit)")

        while True:
            grade = int(input())
            
            if grade == -1:
                break

            grades.append(grade)
        
        return grades    

    def getGradesAverage(self, grades):
        gradesAverage = sum(grades) / len(grades)
        print(f"Your grades average is " + str(gradesAverage) + "    " + str(grades)) 

   
student = Student()
student.inputStudent()
grades = student.inputGrades()
student.welcomeMessage()
student.getGradesAverage(grades)