
# Protected Instacne ==> _"instance name" ==> use kori in concept of java , Only ei page e acess er jonno
# onno page e gele access korte parbe nah
'''
But Python ==> Protected class ta k directly Follow kore
So In conclustion , python folloes only --> Private and Public

'''
class computer :
    def __init__(self):
        self.__processor = 'Corei-9'
        self._ram = '1 TB'
        self.__ssd = '512 GB'
    def show(self):
        print(f"Proceesor : {self.__processor}\nRam : {self._ram}\nSSD : {self.__ssd}")

c1 = computer()
print("Real Configaration is ...")
c1.show()

class Seller:
    def __init__(self):
        # Accessing the Proccesor class
        c1._computer__processor = 'Corei-5'
        c1._ram = '16 GB '
        c1.__ssd = '512 TB'
s1 = Seller()
print("\nAfter Going to Seller...")
c1.show()
