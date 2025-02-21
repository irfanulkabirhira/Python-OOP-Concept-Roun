'Polymorphism Using Abstract Classes (ABC Module)'

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):  # Abstract method
        pass

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Creating objects
cat = Cat()
dog = Dog()

print(cat.speak())  # Output: Meow
print(dog.speak())  # Output: Woof
