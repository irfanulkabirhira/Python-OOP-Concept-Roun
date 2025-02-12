'''
Works on the class itself, not on instances.
Uses cls as the first parameter to access class variables.
Defined using the @classmethod decorator

'''

class Student:
    school = "NITER"  # Class variable (shared by all students)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_school(cls):  # Class method
        return cls.school  # Accessing class variable

# Calling class method without creating an instance
print(Student.get_school())  # ✅ Works because it doesn't depend on an instance
