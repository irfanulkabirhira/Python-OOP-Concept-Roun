class Father:
    def __init__(self, name, work="Unknown"):
        self.name = name
        self.work = work

    def show(self):
        print(f"Father's name: {self.name}, Work: {self.work}")

class Son(Father):
    # Overloading constructor using default arguments
    def __init__(self, name, gf=None, work="Programmer"):
        super().__init__(name, work)  # Call Parent Constructor
        self.gf = gf if gf else "No GF"

    # Overloading-like behavior using default arguments
    def show(self, include_gf=False):
        if include_gf:
            print(f"Son's Name: {self.name}, Work: {self.work}, GF: {self.gf}")
        else:
            print(f"Son's Name: {self.name}, Work: {self.work}")

# Creating Objects
s1 = Son("Hira", "Barsha")  # With GF
s2 = Son("Rahim")  # Without GF

# Calling overloaded methods
s1.show(True)  # Show GF info
s2.show()  # Do not show GF info
