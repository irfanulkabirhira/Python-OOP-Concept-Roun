# Hirrarchical Inheritance ==> in office for sure
'''
class employee:
    pass
class manager(employee):
    pass
class HR (employee):
    pass
class Programmer(employee):
    pass

'''
'''
A Employ class having name and emoloy_id attribute ,
->
And That Employ classed Inherites a HR Class
having extra attribite Department ,
->
same way , Manager , Programmer class having attribite
(Team_size and Programming_language respectiviely)
So Now , Show Everyone's details [ HR , Manger and Programmer]
'''


# Base Class - Employee
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}")

# Child Class 1 - HR
class HR(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)  # Call Employee's constructor
        self.department = department

    def display_hr(self):
        print(f"Department: {self.department}")

# Child Class 2 - Manager
class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)  # Call Employee's constructor
        self.team_size = team_size

    def display_manager(self):
        print(f"Team Size: {self.team_size}")

# Child Class 3 - Programmer
class Programmer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)  # Call Employee's constructor
        self.programming_language = programming_language

    def display_programmer(self):
        print(f"Programming Language: {self.programming_language}")

# Creating objects for each child class
hr1 = HR("Alice", "E001", "Human Resources")
manager1 = Manager("Bob", "E002", 10)
programmer1 = Programmer("Charlie", "E003", "Python")

# Displaying Information for each employee type
print("HR Information:")
hr1.display()
hr1.display_hr()

print("\nManager Information:")
manager1.display()
manager1.display_manager()

print("\nProgrammer Information:")
programmer1.display()
programmer1.display_programmer()




