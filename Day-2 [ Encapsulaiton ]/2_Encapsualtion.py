# Encapsulation ==> Using Private banai dici directly  that is why seller can directly acces the Computer Class
'''
As i created this to ( private), that is why , Seller Can not acces the Computer class
Private ==> __procesor , __ram , __ssd

'''

class Computer:
    def __init__(self):
        self.__processor = 'Corei-9'
        self.__ram = 64
        self.__ssd = '1 TB '
    def show(self):
        print(f"Procesor : {self.__processor}\nRam : {self.__ram}\nSSD : {self.__ssd}")

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