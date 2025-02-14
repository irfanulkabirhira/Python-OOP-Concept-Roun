class Student:  # Class names should be in PascalCase
    def __init__(self):
        self.color = 'blue'  # Instance variable

    def hira(self):  # Added self as the first parameter
        return "This is Hira's Fav Color"

# Creating Object of the Class
obj = Student()  # Creating an instance
print(obj.color)  # Accessing instance variable correctly
print(obj.hira())

