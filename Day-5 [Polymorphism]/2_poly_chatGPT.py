'Polymorphism with Class Methods'
# Class 1
class Cat:
    def speak(self):
        return "Meow"
# Class 2
class Dog:
    def speak(self):
        return "Woof"

# Function that demonstrates polymorphism [Different Class]
def animal_sound(animal):
    print(animal.speak())

# Creating objects
cat = Cat()
dog = Dog()

# Calling the same method on different classes
animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Woof
