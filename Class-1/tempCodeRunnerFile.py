'''
Write a program of a problem where => a class should be created naming => Library which has [no of books] and Books attributes (can be instance attribute, class attributes). Create some obj as book.
Task:
1. Show any one obj details &
2. Book list
'''

class Library:
    book_list = []  # ✅ Class Attribute (Shared by all objects)

    def __init__(self, book_name):
        self.book_name = book_name  # ✅ Instance Attribute

    def show_details(self):  # ✅ Instance Method
        print(f"Book Name: {self.book_name}")

    @classmethod
    def show_all_books(cls):  # ✅ Class Method (Without append)
        print("Book List:", [book.book_name for book in cls.book_list])  # Using list comprehension


# ✅ Creating Book Objects and Storing in Class Attribute
book1 = Library("Python Basics")
book2 = Library("Data Science")
book3 = Library("Machine Learning")

Library.book_list = [book1, book2, book3]  # ✅ Storing objects manually in class attribute

# ✅ Showing details of one book
print("📌 One Book Detail:")
book1.show_details()  # Output: Book Name: Python Basics

# ✅ Showing the full book list
print("\n📌 All Books in Library:")
Library.show_all_books()  # Output: Book List: ['Python Basics', 'Data Science', 'Machine Learning']
