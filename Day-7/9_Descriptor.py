# To set this
class A :
    def __get__(self, instance, owener):
        print("getting")
        return instance.__dict__.get('Attribite', None)
    def __set__(self, instance , value):
        print("Setting")
        instance.__dict__['Attribute'] = value

class myClass:
    Attribite = A()

obj = myClass()
obj.Attribite = 22
print(obj.Attribite)

