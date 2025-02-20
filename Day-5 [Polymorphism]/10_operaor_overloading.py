class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def details(self):
        print(self.title)
        print(self.page)

    def __add__(self, other):
        if not isinstance(other, Book):  # Ensure 'other' is a Book instance
            raise TypeError("Both objects must be of type Book")
        total = self.page + other.page
        return Book("All Books", total)

    def __str__(self):
        return f"Book Title: {self.title}, Pages: {self.page}"  # Improved string representation


b1 = Book("A", 10)
b2 = Book("B", 20)
b3 = Book("C", 10)

total_books = b1 + b2 + b3  # Works now
print("Total no of pages: ", total_books)
