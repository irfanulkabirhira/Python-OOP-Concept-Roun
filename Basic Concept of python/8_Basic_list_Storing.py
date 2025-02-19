class BookStore:
    def __init__(self):
        self.books = ['hira', 'mira', 'tira']

    def order_book(self, book_name):
        if book_name in self.books:
            return f"The book '{book_name}' is available. Your order has been placed!"
        else:
            return f"Sorry, the book '{book_name}' is not available."

    def user_choice(self):
        """Function to let the user choose actions dynamically"""
        while True:
            print("📚 Bookstore Menu:")
            print("1. Order a Book")
            print("2. Exit")

            choice = input("\nEnter your choice (1-2): ").strip()

            if choice == "1":
                book_name = input("Enter the book name you want to order: ").strip().lower()
                print(self.order_book(book_name))

            elif choice == "2":
                print("Thank you for visiting the Bookstore! 📖✨")
                break

            else:
                print("Invalid choice! Please enter 1 or 2.")

# Example Usage
store = BookStore()
store.user_choice()
