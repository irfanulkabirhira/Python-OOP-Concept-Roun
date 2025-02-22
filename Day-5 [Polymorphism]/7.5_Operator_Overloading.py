class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def __add__(self, other):
        total = self.page + other.page
        return Book('all books', total)

    def __str__(self):
        return str(self.page)


b1 = Book('A', 10)
b2 = Book('B', 20)
b3 = Book('C', 10)
s=b1+b2+b3

print("Total no of pages:", s.page)  # Access the 'page' attribute of the resulting Book object
