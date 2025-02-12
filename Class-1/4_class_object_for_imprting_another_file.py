class Student:  # Class names should be in PascalCase
    def __init__(self):
        self.color = 'blue'  # Instance variable

    def hira(self):  # Added self as the first parameter
        return

obj = Student()  # Creating an instance
print(obj.color)  # Accessing instance variable correctly
