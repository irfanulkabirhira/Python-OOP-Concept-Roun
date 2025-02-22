class Book:
    all_books = []  # Store all book instances

    def __init__(self, title, page):
        self.title = title
        self.page = page
        Book.all_books.append(self)  # Add book to list

    @classmethod
    def show_all_books(cls):
        for book in cls.all_books:
            print(book)

    def __add__(self, other):
        return Book(f"{self.title} + {other.title}", self.page + other.page)

    def __str__(self):
        return f"Title: {self.title}, Pages: {self.page}"


b1 = Book("A", 10)
b2 = Book("B", 20)
b3 = Book("C", 10)

Book.show_all_books()  # Display all books
