from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def area(self):
        pass
'''
Ractangle --> class and
print area of Ranctangle

same work for Cericel as well
'''

class Rectangle(Shape):
    def show(self):
        print("This is Rectangle...")
    def area(self , l , r):
        print(f"Area : {l*r} ")

# class circle(Shape):
#     def show(seld):
#         print("This is Circle .....")
#     def area(self):
#         print()

# Object
object = Rectangle()
object.show()
object.area(20 , 10)


