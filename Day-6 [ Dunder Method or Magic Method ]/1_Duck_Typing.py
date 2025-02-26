class Animal :
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Gheu gheu ")

class Cat(Animal):
    def make_sound(self):
        print("Meu Meu")

# Duck Typing
class Car(Animal):
    def make_sound(self):
        print("Pip pip")

car1 = Car()
d1 = Dog()
c1 = Cat()

c1.make_sound()
d1.make_sound()
car1.make_sound()