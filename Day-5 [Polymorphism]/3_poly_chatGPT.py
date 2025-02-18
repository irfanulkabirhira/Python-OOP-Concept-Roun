'Method Overriding in Inheritance'
class Animal:
    def speak(self):
        return "Some sound"

# cat is inherited from Animal Class
class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Creating objects
animal = Animal()
cat = Cat()
dog = Dog()

# Calling the overridden method
print(animal.speak())  # Output: Some sound
print(cat.speak())     # Output: Meow
print(dog.speak())     # Output: Woof
