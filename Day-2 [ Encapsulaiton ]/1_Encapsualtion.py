# Encapsulation ==> Used Public that is why seller can directly acces the Computer Class too

class Computer:
    def __init__(self):
        self.processor = 'Corei-9'
        self.ram = 64
        self.ssd = '1 TB '
    def show(self):
        print(f"Procesor : {self.processor}\nRam : {self.ram}\nSSD : {self.ssd}")

c1= Computer()
print("Real Configaration ...")
c1.show()

class Seller:
    def __init__(self):
        c1.processor = 'Corei-5'
        c1.ram = 16
        c1.ssd = '512 GB '
s1 = Seller()
print("\nAfter Modifying the Configaraiton :")
c1.show()