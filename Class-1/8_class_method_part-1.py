'''
Uses @classmethod decorator.
First parameter is cls (not self).
Can access and modify class attributes.
'''

class Student:
    university = "NITER"  # Class attribute

    @classmethod
    def change_university(cls, new_uni):
        cls.university = new_uni  # Changing class attribute

# Calling class method without creating an instance
Student.change_university("Khulna University")
print(Student.university)  # ✅ Output: Khulna University
