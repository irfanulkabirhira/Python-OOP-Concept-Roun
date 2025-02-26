# To set this
class A :
    def __get__(self, instance, owener):
        print("getting")
        return instance.__dict__.get('Attribite', None)
    def __set__(self, instance , value):
        print("Setting")
        instance.__dict__['Attribite'] = value
    def __delete__(self, instance):
        print("Deleting")
        del instance.__dict__['Attribite']

class myClass:
    Attribite = A()

obj = myClass()
obj.Attribite = 22
del obj.Attribite
print(obj.Attribite)

