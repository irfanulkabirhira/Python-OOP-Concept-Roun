class Library:
    book_list = []  # ✅ Class Attribute (Shared by all objects)

    def __init__(self, book_name):
        self.book_name = book_name  # ✅ Instance Attribute
        Library.book_list.append(book_name)  # ✅ Adding book to the shared list

    def show_details(self):  # ✅ Instance Method
        print(f"Book Name: {self.book_name}")

    @classmethod
    def show_all_books(cls):  # ✅ Class Method
        print("Book List:", cls.book_list)


# ✅ Creating Book Objects
book1 = Library("Python Basics")
book2 = Library("Data Science")
book3 = Library("Machine Learning")

# ✅ Showing details of one book
print("📌 One Book Detail:")
book1.show_details()  # Output: Book Name: Python Basics

# ✅ Showing the full book list
print("\n📌 All Books in Library:")
Library.show_all_books()  # Output: Book List: ['Python Basics', 'Data Science', 'Machine Learning']
