
class Cat:
    def speak(self):
        return "Hi this , Cat Meu Meu !!!"
class Dog:
    def speak(self):
        return "Hello This is Dog , gheu Ghue !!!"

# For Both of the Class i am Creatng an Common method name==> Sound_Animal
# And pssing an peramiter Animal Here
def sound_animal(animal):
    print(animal.speak())
cat = Cat()
dog = Dog()

sound_animal(cat)
sound_animal(dog)