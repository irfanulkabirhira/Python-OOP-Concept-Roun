'Method Overloading using *args (Flexible Arguments)'
class MathOperations:
    def add(self, *args):  # Accepts multiple arguments
        return sum(args)

# Creating an object
math_op = MathOperations()

# Calling the method with different numbers of arguments
print(math_op.add(5))         # Output: 5
print(math_op.add(5, 10))     # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30
print(math_op.add(1, 2, 3, 4, 5)) # Output: 15
