'''

Uses self as the first parameter.
Can access and modify instance attributes.
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):  # Regular instance method
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Hira", 25)
student1.display()  # ✅ Works because 'self' refers to student1
