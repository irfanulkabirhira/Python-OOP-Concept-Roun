#-> hybrid => uporer gular , More than 1 applied hole , Hybrid
# Base Class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Base Class 2 (Inheritance from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call to Person's constructor
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

# Intermediate Class (Multiple Inheritance: Inheriting from Person and Student)
class Employee(Student, Person):
    def __init__(self, name, age, student_id, employee_id):
        Student.__init__(self, name, age, student_id)  # Calling Student's constructor
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")

# Derived Class (Hybrid Inheritance: Inheriting from Employee and Person)
class Intern(Employee):
    def __init__(self, name, age, student_id, employee_id, internship_duration):
        Employee.__init__(self, name, age, student_id, employee_id)  # Calling Employee's constructor
        self.internship_duration = internship_duration

    def display_intern(self):
        self.display()  # Calling Person's display method
        print(f"Student ID: {self.student_id}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Internship Duration: {self.internship_duration} months")

# Creating an Intern Object
intern1 = Intern("Hira", 25, "S123", "E456", 6)

# Displaying Information
intern1.display_intern()
