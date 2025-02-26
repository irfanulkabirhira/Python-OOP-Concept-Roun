# Method over_loading does not Support that much Accuratly in Pyton OOP 
class Addition:
    def sum(self, a, b):
        return a+b
    def sum(self , a, b , c):
        return a+b+c

obj1 = Addition()
obj2 = Addition()
print(obj1.sum(1,2))
print(obj2.sum(1, 2, 3))
