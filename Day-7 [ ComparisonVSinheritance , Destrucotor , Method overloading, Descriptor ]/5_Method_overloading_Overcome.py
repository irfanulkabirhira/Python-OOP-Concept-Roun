# To Overcome the Method Overloading Problem
# Method over_loading does not Support that much Accuratly in Pyton OOP
class Addition:
    def sum(self , a , b = None , c = None):
        if (a!=None and b!=None and c!=None):
            return a+b+c
        elif(a!=None and b!=None):
            return a+b
        else:
            return a


obj1 = Addition()
obj2 = Addition()

print(obj1.sum(1,2))
print(obj2.sum(1, 2, 3))
'this is how we handle method overloading in Python oop concept'
