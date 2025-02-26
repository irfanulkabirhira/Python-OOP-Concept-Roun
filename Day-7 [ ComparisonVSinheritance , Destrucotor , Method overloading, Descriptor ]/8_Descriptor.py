# To get this 
class A :
    def __get__(self, instance, owener):
        print("getting")
        return instance.__dict__.get('Attribite', None)

class myClass:
    Attribite = A()

obj = myClass()
print(obj.Attribite)

