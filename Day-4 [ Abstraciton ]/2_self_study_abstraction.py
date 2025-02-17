'''
Abstract class is class where at least one abstract method should be exist
there can be either Concreter method or abstract mehtod
But Note it down [At least One Abstrat must there for sure  ]
Note it Down :
--------------
==> we can not crete Abstract class object
According to Campasuc Sir , it's one most least use OOP principle

'''
# Abstract Class
from abc import ABC, abstractmethod
class BankManger(ABC):
    def Database(self):
        print('Conected to the Databases')
    @abstractmethod
    def security(self):
        pass
    @abstractmethod
    def display(self):
        pass

# Concrete method (Inheritace) or concrete class
class Mobilemanager(BankManger):
    print('Login into to the Mobile Device')
    def security(self):
        print('MObile Security is on')

    def display(self):
        print('Displaying all work')

object = Mobilemanager()