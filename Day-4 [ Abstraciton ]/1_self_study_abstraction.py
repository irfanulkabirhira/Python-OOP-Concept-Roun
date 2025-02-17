'''
Abstract class is class where at least one abstract method should be exist
there can be either Concreter method or abstract mehtod
But Note it down [At least One Abstrat must there for sure  ]
Note it Down :
--------------
==> we can not crete Abstract class object
According to Campasuc Sir , it's one most least use OOP principle 
'''
# Abstract Method
from abc import ABC , abstractmethod
# abstract method
class BankManager(ABC):
    def database(self):
        print('Connected to Database')
    @abstractmethod
    def security(self):
        pass

# Inheritance or ( Concrete Method )
class Mobilemaneger(BankManager):
    print('Login to the Mobile Device')

    def security(self):
        print('Mobile Security')

object = Mobilemaneger()