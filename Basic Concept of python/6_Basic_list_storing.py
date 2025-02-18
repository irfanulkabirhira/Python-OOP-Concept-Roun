class Library:
    Book = []
    def __init__(self , BookName , Nu_Book):
        self.BookName = BookName
        self.Nu_Book = Nu_Book
        if self.BookName not in self.Book:
            self.Book.append(self.BookName)


    def showBook(self):
        print(f"Books are :{self.Book}\nNumber of Books based on this topic:{self.Nu_Book} ")


object1 = Library('Break Up Story',  3)
object1 = Library("Life is okay ", 34)

object1.showBook()

# To see the Details
print(object1.__dict__)