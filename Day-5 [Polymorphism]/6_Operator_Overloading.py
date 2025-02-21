# Operator overloading

'''
add ==>
sum ==>
div ==>
mul ==>

__add__ , __sub__ ,__mul__ ==> This are magic method

'''
num1 = 10
num2 = 20

# For adding the
print(num1 + num2)
print(num1.__add__(num2))
print("The Summation Is :",int.__add__(num1, num2))

# For subtraction
print("The Substraction is :",int.__sub__(num2, num1))

# for Multiplation
print("The Multiplacation is :",int.__mul__(num1,num2))

