from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # Abstract Method
        pass

    def leg(self):  # Concrete Method
        print("Animals have legs")

# Concrete Class Dog
class Dog(Animal):
    def make_sound(self):
        print("Gheu Gheu !!")

# Concrete Class Cat
class Cat(Animal):
    def make_sound(self):
        print("Meu Meu !!")

    # Method Overriding
    def leg(self):
        print("It has 4 Legs")

# Creating Objects
animal1 = Cat()
animal2 = Dog()

# Calling Methods
animal1.make_sound()  # Output: Meu Meu !!
animal2.leg()  # Output: Animals have legs

print(isinstance(animal1, Cat))  # Output: True
