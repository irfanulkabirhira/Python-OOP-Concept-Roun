class Library:

    # To Accept Multiple Books
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
    def add_books(cls, *book_names):  # Accept multiple book names
        for book in book_names:
            if book not in cls.Book:
                cls.Book.append(book)

# Creating objects
b1 = Library(1, "Hira")
b2 = Library(2, "Jira")

# Adding multiple books at once
Library.add_books("Kira", "Tira", "Mira", "Lira")  # Corrected function call

# Task 1
b2.showbook()

# Show details
# print(b1.__dict__)  # Shows instance attributes
