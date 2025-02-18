class Library:
    Book = ['Hira', 'Jira', 'Mira', 'Kira']  # Class-level book list

    def __init__(self, Book_Name, Nu_Book):
        self.Book_name = Book_Name
        self.Nu_Book = Nu_Book

        if self.Book_name in Library.Book:  # Corrected class variable access
            print(f"'{self.Book_name}' is available in the list.")
        else:
            print(f"'{self.Book_name}' is not available in the list.")

    def show(self):
        print(f"Book Name: {self.Book_name}, Number of Books: {self.Nu_Book}")

# Creating objects
object1 = Library('Hira', 25)
object2 = Library('Tania', 24)

# Display object details
object1.show()
object2.show()

# Print object dictionary
print(object1.__dict__)
