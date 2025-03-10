
"""
class Student:
    def __init__(self, name , age, university):
        self.name = name
        self.age = age
        self.university =university

    def display(self):
        print(f"Name : {self.name} , Age : {self.age} , Univeristy : {self.university}")

student1 = Student("Hira", 25 , "NITER")
student2 = Student("Mita", 24, "NITER")

# Calling the Method
student1.display()
student2.display()

"""
# Here we Can see , Uni is Common for both of the Student , So will use Global variable here

class Student:
    # Global varibale
    university = "NITER" #Class Attribite

    def __init__(self, name , age):
        #local varible or Attribte
        self.name = name # instance attribite
        self.age = age # Instance Attribite

    def display(self): #instance Method or regular instnace method
        print(f"Name : {self.name} , Age : {self.age} , Univeristy : {self.university}")
        print(self.name)

student1 = Student("Hira", 25 )
student2 = Student("Mita", 24)

# Calling the Method
student1.display()
student2.display()
# Only to Print Specific Instance Variable
print(f"Only Printing their name {student1.name}")