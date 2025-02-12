'''
Uses @staticmethod decorator.
No self or cls, meaning it does not access instance or class variables.
Works like a normal function inside a class.
'''
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Calling static method
result = MathOperations.add(10, 5)
print(result)  # ✅ Output: 15
