# Hirarchy Inheritacne
# Base Class - Parent (Common attributes for both father and mother)
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent's Name: {self.name}")

# Derived Class 1 - Father (Inherits from Parent)
class Father(Parent):
    def __init__(self, name, occupation):
        super().__init__(name)  # Initialize Parent class
        self.occupation = occupation

    def display_father(self):
        print(f"Father's Occupation: {self.occupation}")

# Derived Class 2 - Mother (Inherits from Parent)
class Mother(Parent):
    def __init__(self, name, occupation):
        super().__init__(name)  # Initialize Parent class
        self.occupation = occupation

    def display_mother(self):
        print(f"Mother's Occupation: {self.occupation}")

# Child Class - Sibling (Inherits from both Father and Mother)
class Sibling(Father, Mother):
    def __init__(self, name, father_name, father_occupation, mother_name, mother_occupation):
        Father.__init__(self, father_name, father_occupation)  # Initialize Father
        Mother.__init__(self, mother_name, mother_occupation)  # Initialize Mother
        self.name = name

    def display_child(self):
        print(f"Child's Name: {self.name}")

# Creating Sibling objects (You can create one for each sibling)
hira = Sibling("Hira", "Abu Taher", "Businessman", "Laila Begum", "Housewife")
humayun = Sibling("Humayun Kabir Manik", "Abu Taher", "Businessman", "Laila Begum", "Housewife")
taslima = Sibling("Taslima", "Abu Taher", "Businessman", "Laila Begum", "Housewife")

# Displaying information for Hira
print("Information for Hira:")
hira.display_child()
hira.display_father()
hira.display_mother()

# Displaying information for Humayun
print("\nInformation for Humayun:")
humayun.display_child()
humayun.display_father()
humayun.display_mother()

# Displaying information for Taslima
print("\nInformation for Taslima:")
taslima.display_child()
taslima.display_father()
taslima.display_mother()
