class Student:
    # Global varibale
    university = "NITER" #Class Attribite

    def __init__(self, name , age):

        #local varible or Attribte
        self.name = name # instance attribite
        self.age = age # Instance Attribite

    def display(self): #instance Method
        print(f"Name : {self.name} , Age : {self.age} , Univeristy : {self.university}")

student1 = Student("Hira", 25 )
student2 = Student("Mita", 24)

# Calling the Instance Method
student1.display()
student2.display()