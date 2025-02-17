# Single Inheritace => single parent single Child
'''
class employee:
    pass
class manager(employee):
    pass

'''

'''
A preson having name and age attribute , And That person Inherites a student Class
and stuedent extented his attribute with studen_id ,
So Now , show the Student Class Details

'''
# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the Person class
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

# Creating a Student Object
student1 = Student("Hira", 25, "S123")

# Displaying Information
student1.display()  # Calls the method from Person class
student1.display_student()  # Calls the method from Student class
