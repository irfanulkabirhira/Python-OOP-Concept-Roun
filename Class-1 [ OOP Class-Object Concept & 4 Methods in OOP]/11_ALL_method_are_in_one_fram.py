class Student:
    university = "NITER"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # ✅ Instance Method (uses `self`, can access instance attributes)
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, University: {self.university}")

    # ✅ Class Method (uses `cls`, can modify class attributes)
    @classmethod
    def change_university(cls, new_uni):
        cls.university = new_uni

    # ✅ Static Method (doesn't use `self` or `cls`)
    @staticmethod
    def add_numbers(a, b):
        return a + b

# ✅ Regular Method (Standalone function, outside the class)
def greet():
    print("Hello, welcome to the Python class!")

# -------------------
# 🚀 Using all methods
# -------------------

# Creating an instance
student1 = Student("Hira", 25)

# Calling instance method
student1.display_info()  # ✅ Name: Hira, Age: 25, University: NITER

# Calling class method
Student.change_university("Khulna University")
print(Student.university)  # ✅ Khulna University

# Calling static method
result = Student.add_numbers(10, 5)
print(result)  # ✅ Output: 15

# Calling regular method
greet()  # ✅ Output: Hello, welcome to the Python class!
