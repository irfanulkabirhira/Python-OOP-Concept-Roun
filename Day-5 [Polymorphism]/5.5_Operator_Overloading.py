'''
add ==>
sum ==>
div ==>
mul ==>

__add__ , __sub__ ,__mul__ ==> This are magic method

'''
class A :
    def __init__(self, x):
        self.x= x

    def __add__(self, other):
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x=x


# Creating Object
a=A(100)
b=B(200)

print(a+b)