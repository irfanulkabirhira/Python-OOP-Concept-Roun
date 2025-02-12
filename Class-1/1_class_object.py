class faculty:
    def putdata(self): # method 1
        # attribute
        self.id = int(input("Enter Your ID "))
        self.name = input("Enter Your name ")
        self.salary = float(input("Enter Your Faculty Salary "))

    def display(self): # Mehtod 2
        print("Faculty id :", self.id)
        print("Faculty name :",self.name)
        print("Faculty Salary:",self.salary)

# Creating Object of this faculty Class
a = faculty()
a.putdata()
a.display()




