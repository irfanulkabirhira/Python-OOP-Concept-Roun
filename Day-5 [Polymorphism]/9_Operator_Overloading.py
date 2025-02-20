class Cart:
    def __init__(self, busket1, busket2, busket3):
        self.clothes = busket1
        self.electronics = busket2
        self.other = busket3

    def get_details(self):
        print("clothes: ", self.clothes)
        print("electronics: ", self.electronics)
        print("other: ", self.other)

    def __len__(self):
        return len(self.clothes) + len(self.electronics) + len(self.other)

customer1 = Cart(['jeans', 't-shirt', 'cap'], ['mobile', 'charger'], ['dining table'])
customer2 = Cart(['jeans', 't-shirt', 'cap'], ['mobile', 'charger'], ['dining table'])

print(len(customer1))  # Output: 6
print(len(customer2))  # Output: 6
