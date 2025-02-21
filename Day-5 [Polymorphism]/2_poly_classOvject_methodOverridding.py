'Polymorphism with Class Methods'


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
# method Over_ridding
sound_animal(dog)


'''
I can Show this like as well
----------------------------------
def sound_animal(animal):
    animal.speaK()


sound_animal(cat)
sound_animal(dog)

'''
