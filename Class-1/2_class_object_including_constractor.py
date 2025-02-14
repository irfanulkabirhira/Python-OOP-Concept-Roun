# Class Object Including Contractor  :

class faculty:
    # Constractor ==> this will automatically initialize the method
    def __init__(self):
        self.id = int(input("Enter Your ID "))
        self.name = input("Enter Your Name ")
        self.salary = float(input("Enter your Salary amount "))

    def dispaly(self):
        print("Faculty ID is = ", self.id)
        print("Name is = ", self.name)
        print("Salary is  = ", self.salary)


# Creating an object of Faculty class
a = faculty()
b = faculty()
a.dispaly()


