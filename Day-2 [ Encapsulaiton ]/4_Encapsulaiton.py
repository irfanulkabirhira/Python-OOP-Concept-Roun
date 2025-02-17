# But Python Indirectly Access korte dei ==> private class k
# I can access the private class through ==> _"classname"  [Lol] ==> that's is why python does not follow the Encapsulation Concept properly
class computer :
    def __init__(self):
        self.__processor = 'Corei-9'
        self.__ram = '1 TB'
        self.__ssd = '512 GB'
    def show(self):
        print(f"Proceesor : {self.__processor}\nRam : {self.__ram}\nSSD : {self.__ssd}")

c1 = computer()
print("Real Configaration is ...")
c1.show()

class Seller:
    def __init__(self):
        # Accessing the Proccesor class
        c1._computer__processor = 'Corei-5'
        c1.__ram = '16 GB '
        c1.__ssd = '512 TB'
s1 = Seller()
print("\nAfter Going to Seller...")
c1.show()
