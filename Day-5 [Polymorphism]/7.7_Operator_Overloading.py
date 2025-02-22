class Book:
    book_count = 0  # Class variable to assign unique IDs

    def __init__(self, title, page, author="Unknown"):
        Book.book_count += 1
        self.id = Book.book_count
        self.title = title
        self.page = page
        self.author = author

    def __add__(self, other):
        combined_title = f"{self.title} + {other.title}"
        combined_pages = self.page + other.page
        return Book(combined_title, combined_pages, "Multiple Authors")

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Pages: {self.page}"


b1 = Book("A", 10, "Author 1")
b2 = Book("B", 20, "Author 2")
b3 = Book("C", 10, "Author 3")

print("Total:", b1 + b2 + b3)
