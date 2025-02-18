'Overloading the * Operator (__mul__ Method)'
class Product:
    def __init__(self, price):
        self.price = price

    def __mul__(self, quantity):  # Overloading *
        return self.price * quantity

# Creating a Product object
item = Product(100)

# Multiplying price by quantity
total_price = item * 5  # Calls __mul__()
print(total_price)  # Output: 500
