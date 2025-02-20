# Add Search for a Book Opiton

class BookStore:
    def __init__(self):
        self.books = ['hira', 'mira', 'tira']
        self.removed_books = []  # Store removed books for restocking
        self.sales_history = []  # Track sales history

    def order_book(self, book_name):
        """Allows a user to order a book if available."""
        if book_name in self.books:
            self.sales_history.append(book_name)  # Add order to sales history
            return f"📦 The book '{book_name}' is available. Your order has been placed!"
        else:
            return f"❌ Sorry, the book '{book_name}' is not available."

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
            self.removed_books.append(book_name)  # Save for possible restock
            print(f"🗑️ The book '{book_name}' has been removed.")
        else:
            print(f"⚠️ The book '{book_name}' is not available in the store.")

    def restock_book(self, book_name):
        """Admin feature to restock a previously removed book."""
        if book_name in self.removed_books:
            self.books.append(book_name)
            self.removed_books.remove(book_name)
            print(f"📦 The book '{book_name}' has been restocked!")
        else:
            print(f"⚠️ The book '{book_name}' is not in the removed list.")

    def view_sales_history(self):
        """Displays the history of ordered books."""
        if self.sales_history:
            print("\n📜 Sales History:")
            for index, book in enumerate(self.sales_history, start=1):
                print(f"{index}. {book}")
        else:
            print("\n📜 No sales history available.")

    def view_books(self):
        """Displays all available books."""
        if self.books:
            print("\n📖 Available Books:", ", ".join(self.books))
        else:
            print("\n📖 No books available at the moment.")
    def