# hybrid => uporer gular , More than 1 applied hole , Hybrid

class Person:
    # Constractor that initializing the method
    def __init__(self, name, age):
        self.name = name # Instance Attribite
        self.age = age # Instance Attribute

    def display(self): # Instance Method
        print(f"Name: {self.name}, Age: {self.age}")

# Intermediate Class 1 - Inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

# Intermediate Class 2 - Inheriting from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")

# Derived Class - Inheriting from both Student and Employee (Hybrid Inheritance)
class Intern(Student, Employee):
    def __init__(self, name, age, student_id, employee_id, internship_duration):
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, name, age, employee_id)
        self.internship_duration = internship_duration

    def display_intern(self):
        self.display()  # Calling Person's display method
        print(f"Internship Duration: {self.internship_duration} months")

# Creating an Intern Object
intern1 = Intern("Hira", 25, "S123", "E456", 6)

# Displaying Information
intern1.display_intern()
