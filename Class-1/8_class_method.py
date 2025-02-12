class Stuedent:
    # Global varibale
    University = 'NITER'

    def __init__(self, name , age):
        # Local Variable
        self.name = name # Instane Attribite
        self.age = age

    def show(self): # Regular Instance Method
        print(f"The Univeristy name is : {self.University}")

    @classmethod # Class Method
    def changeUniversity(cls, uni):


obj1 = Stuedent('Hira', 25)
obj1.show()

