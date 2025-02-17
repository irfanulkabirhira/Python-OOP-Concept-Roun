'''
==> Write a program of a problem where => a class should be created naming => Library which has[no of  books] and Books attributes (can be instance attribute, class attributes). Create some obj as book.
    Task:
    1. Show any one obj details &
    2. Book list
'''

# Sir's Solved
class Library :
    # Instance Attribite
    Book = []
    def __init__(self, nu_book , book_name):
        self.nu_book = nu_book
        self.book_name = book_name
        if self.book_name not in self.Book:
            self.Book.append(self.book_name)

    def showbook(self):
        print(self.Book)

    def add_book(cls , Book):
        cls.Book = Book


b1 = Library(1 , "Hira")
b2 = Library(2, "Jira")

# Task 1
b1.showbook()
# show detasils
print(b1.__dict__)