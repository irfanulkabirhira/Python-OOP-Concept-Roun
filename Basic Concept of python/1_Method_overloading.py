'Method Overloading using Default Arguments'
class MathOperations:
    def add(self, a, b=0, c=0):  # Default arguments
        return a + b + c

# Creating an object
math_op = MathOperations()

# Calling the same method with different numbers of arguments
print(math_op.add(5))         # Output: 5
print(math_op.add(5, 10))     # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30

