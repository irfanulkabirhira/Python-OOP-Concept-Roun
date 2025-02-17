'''
Write a program of a problem where => a class should be created naming Library  =>
which has [no of books] and Books attributes (can be instance attribute, class attributes). Create some obj as book.
Task:
1. Show any one obj details &
2. Book list
'''
class Library:
    # Clas Attribtue
    book_list = ["Hira", "Jira"]

    # Constractor
    def __init__(self, no_book ):
        # Instance Attribute
        self.no_book = no_book
    def display(self):
        print(f"The Number of books is {self.no_book}")


    def book_details(self,books):
        if books in self.book_list:
            self.append(books)
        else:
            print(f"{books} are not in the list ")

    def show_book_list(self):
        print(f"The list of the Books are {self.book_list}")

# Creating an object and passing required argument
object = Library(5)
object.display()

object.show_book_list()

object.book_details("New book")
object.show_book_list

