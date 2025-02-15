# if i want to print Only name except using extra function
'''
def setName (self , name):
        self.name = name

Solutaoitn :
In the son class constructor, I used super().__init__(name, "Unknown") to call the parent father class's constructor properly and assign the name. Since you only need the name and not work for printing, I’ve used "Unknown" as a placeholder.

'''

class father:
    def __init__(self, name , work):
        self.name = name
        self.work = work
        self.home = 'Owned'

    def show(self):
        print(f"name is :{self.name} , age is :{self.work}")


class son(father):
    def __init__(self, name, gf):
        super().__init__(name, "Unknown")  # Calling the parent constructor
        self.gf = gf

    def show(self):
        print(f"name is :{self.name} , age is :{self.work} , and GF is : {self.gf}")

# Creating object
S = son('Hira', 'Barsha')

# Printing only the name
print(S.name)
