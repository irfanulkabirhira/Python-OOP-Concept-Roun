class Library:
    # Class Attribute
    Book = []

    def __init__(self, nu_book, book_name):
        self.nu_book = nu_book
        self.book_name = book_name
        if self.book_name not in Library.Book:
            Library.Book.append(self.book_name)  # Correct way to append to class attribute

    def showbook(self):
        print(self.Book)

    @classmethod  # Use classmethod decorator
    def add_book(cls, book_name):
        if book_name not in cls.Book:
            cls.Book.append(book_name)

# Creating objects
b1 = Library(1, "Hira")
b2 = Library(2, "Jira")

# Fixing the incorrect function call
Library.add_book("Kira")  # Corrected function call

# Task 1
b1.showbook()

# Show details
print(b1.__dict__)  # Shows instance attributes
