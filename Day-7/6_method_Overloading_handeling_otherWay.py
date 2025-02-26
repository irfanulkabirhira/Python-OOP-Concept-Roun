class Addition:
    def sum(self, *numbers):
        total = 0
        for x in numbers:
            total = total + x
        return total

obj1 = Addition()
obj2 = Addition()

print(obj1.sum(1,2))
print(obj2.sum(1, 2, 3))