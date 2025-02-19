# Adding and Removinhg Funciton added here

class BookStore:
    def __init__(self):
        self.books = ['hira', 'mira', 'tira']

    def order_book(self, book_name):
        """Allows a user to order a book if available."""
        if book_name in self.books:
            return f"The book '{book_name}' is available. Your order has been placed!"
        else:
            return f"Sorry, the book '{book_name}' is not available."

    def add_book(self, book_name):
        """Admin feature to add a new book to the store."""
        if book_name not in self.books:
            self.books.append(book_name)
            print(f"✅ The book '{book_name}' has been added successfully!")
        else:
            print(f"⚠️ The book '{book_name}' is already in the store.")

    def remove_book(self, book_name):
        """Admin feature to remove a book from the store."""
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"🗑️ The book '{book_name}' has been removed.")
        else:
            print(f"⚠️ The book '{book_name}' is not available in the store.")

    def view_books(self):
        """Displays all available books."""
        if self.books:
            print("\n📖 Available Books:", ", ".join(self.books))
        else:
            print("\n📖 No books available at the moment.")

    def user_choice(self):
        """Function to let the user choose actions dynamically"""
        while True:
            self.view_books()  # Show available books before menu

            print("\n📚 Bookstore Menu:")
            print("1. Order a Book")
            print("2. Add a New Book (Admin)")
            print("3. Remove a Book (Admin)")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == "1":
                book_name = input("Enter the book name you want to order: ").strip().lower()
                print(self.order_book(book_name))

            elif choice == "2":
                book_name = input("Enter the new book name to add: ").strip().lower()
                self.add_book(book_name)

            elif choice == "3":
                book_name = input("Enter the book name to remove: ").strip().lower()
                self.remove_book(book_name)

            elif choice == "4":
                print("Thank you for visiting the Bookstore! 📖✨")
                break

            else:
                print("Invalid choice! Please enter 1-4.")

# Example Usage
store = BookStore()
store.user_choice()
