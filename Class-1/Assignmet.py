'''
==> Write a program of a problem where => a class should be created naming => Library which has[no of  books] and Books attributes (can be instance attribute, class attributes). Create some obj as book.
    Task:
    1. Show any one obj details &
    2. Book list
'''

class Library:
    # class Attribute
    Book_list = []
    def __init__(self, Book_name):
        self.Book_name = Book_name # Instance Attribute

    def Detail_of_books(self):
        print(f"Name of the book is = {self.Book_name}")

# Creating object of books
book1 = Library("Hira and Sara's Love Story")
book1 = Library("Hira and Barsha's Love Story")

print(" One Book Detail:")
book1.Detail_of_books()



