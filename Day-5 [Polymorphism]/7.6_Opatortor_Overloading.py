class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def __add__(self, other):
        total_title = f"{self.title} + {other.title}"  # Combine titles
        total_pages = self.page + other.page  # Sum pages
        return Book(total_title, total_pages)

    def __str__(self):
        return f"Title: {self.title}, Pages: {self.page}"


b1 = Book('A', 10)
b2 = Book('B', 20)
b3 = Book('C', 10)

print("Total:", b1 + b2 + b3)
