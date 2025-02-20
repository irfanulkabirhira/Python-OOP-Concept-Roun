'''
ekahne j 2 ta method ache 2 ta kei ami
over-ride korci
--> make_sound And Leg 

'''


from abc import ABC , abstractmethod

def Animal(ABC):
    @abstractmethod
    def make_sound(self): # Abstract Method
        pass
    def leg(self): # Concrete method
        pass

def Dog(Animal):
    def make_sound(self):
        print("Gheu Gheu !!")

def Cat(Animal):
    def make_sound(self):
        print("Meu Meu !!")

    # Mehtod Over-Ridding
    def leg(self):
        print("It has 4 Lags")


animal1 = Cat()
animal2 = Dog()

animal1.make_sound(Cat)
animal2.leg()

print(isinstance(animal1 , Dog))
