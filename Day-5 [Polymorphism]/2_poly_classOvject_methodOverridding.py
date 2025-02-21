'Polymorphism with Class Methods'
'''
Method Over-ridding ==>
As you can seee i have used speak funciton for
for Multiple times
here Speak funciton same But they are Doing
differenet taks
That's why for Speak funtion ==> we can say
[ method Over-ridding]
'''
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
