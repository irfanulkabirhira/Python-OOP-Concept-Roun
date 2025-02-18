'Overloading the + Operator (__add__ Method)'
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # String representation
        return f"({self.x}, {self.y})"

# Creating two points
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using the + operator
result = p1 + p2  # Calls __add__()
print(result)  # Output: (6, 8)

