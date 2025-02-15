# hybrid => uporer gular , More than 1 applied hole , Hybrid

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")

class Intern(Student, Employee):
    def __init__(self, name, age, student_id, employee_id, internship_duration):
        # Explicitly call both parent constructors
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, name, age, employee_id)
        self.internship_duration = internship_duration

    def display_intern(self):
        self.display()
        print(f"Student ID: {self.student_id}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Internship Duration: {self.internship_duration} months")

# Creating an Intern Object
intern1 = Intern("Hira", 25, "S123", "E456", 6)

# Displaying Information
intern1.display_intern()


