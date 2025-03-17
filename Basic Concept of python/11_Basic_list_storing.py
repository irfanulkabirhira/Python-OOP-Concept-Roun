# Restoring book here
class BookStore:
    def __init__(self):
        self.books = ['hira', 'mira', 'tira']
        self.removed_books = []  # Store removed books for restocking

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
            return f"✅ The book '{book_name}' has been added successfully!"
        else:
            return f"⚠️ The book '{book_name}' is already in the store."

    def remove_book(self, book_name):
        """Admin feature to remove a book from the store."""
        if book_name in self.books:
            self.books.remove(book_name)
            self.removed_books.append(book_name)  # Save for possible restock
            return f"🗑️ The book '{book_name}' has been removed."
        else:
            return f"⚠️ The book '{book_name}' is not available in the store."

    def restock_book(self, book_name):
        """Admin feature to restock a previously removed book."""
        if book_name in self.removed_books:
            self.books.append(book_name)
            self.removed_books.remove(book_name)
            print(f"📦 The book '{book_name}' has been restocked!")
        else:
            print(f"⚠️ The book '{book_name}' is not in the removed list.")

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
            print("4. Restock a Book (Admin)")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                book_name = input("Enter the book name you want to order: ").strip().lower()
                print(self.order_book(book_name))

            elif choice == "2":
                book_name = input("Enter the new book name to add: ").strip().lower()
                print(self.add_book(book_name))

            elif choice == "3":
                book_name = input("Enter the book name to remove: ").strip().lower()
                print(self.remove_book(book_name))

            elif choice == "4":
                book_name = input("Enter the book name to restock: ").strip().lower()
                self.restock_book(book_name)

            elif choice == "5":
                print("Thank you for visiting the Bookstore! 📖✨")
                break

            else:
                print("Invalid choice! Please enter 1-5.")

# Example Usage 
store = BookStore()
store.user_choice()
