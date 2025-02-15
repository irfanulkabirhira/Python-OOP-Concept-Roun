# Multiple Inheritance --> example is me (Multiple Parent , Single Child)
'''
class Father:
    pass
class Mother:
    pass
# Intermediate Class  - inheriting from father and Mother
class child(Father, Mother):
    pass

'''

# Base Class 1 - Father
class Father:
    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def display_father(self):
        print(f"Father's Name: {self.father_name}, Age: {self.father_age}")

# Base Class 2 - Mother
class Mother:
    def __init__(self, mother_name, mother_age):
        self.mother_name = mother_name
        self.mother_age = mother_age

    def display_mother(self):
        print(f"Mother's Name: {self.mother_name}, Age: {self.mother_age}")

# Child Class - Hira (Inherits from Father and Mother)
class Hira(Father, Mother):
    def __init__(self, name, father_name, father_age, mother_name, mother_age):
        Father.__init__(self, father_name, father_age)  # Initialize Father
        Mother.__init__(self, mother_name, mother_age)  # Initialize Mother
        self.name = name

    def display_child(self):
        print(f"Child's Name: {self.name}")

# Creating an object of the child class (Hira)
hira = Hira("Hira", "AbuTaher", 58, "Laila Begum", 55)

# Displaying Information
hira.display_child()  # Display child's name
hira.display_father()  # Display father's details
hira.display_mother()  # Display mother's details
