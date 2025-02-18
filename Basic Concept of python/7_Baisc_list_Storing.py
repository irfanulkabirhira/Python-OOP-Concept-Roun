
'''
strip(): Removes leading and trailing spaces from the input.
input_text = "  hira  "
print(input_text.strip())  # Output: "hira"
====================================================================
lower(): Converts the input to lowercase.
input_text = "HIRA"
print(input_text.lower())  # Output: "hira"

'''

class BookStore:
    def __init__(self):
        self.books = ['hira', 'mira', 'tira']

    def order_book(self, book_name):
        if book_name in self.books:
            return f"The book '{book_name}' is available. Your order has been placed!"
        else:
            return f"Sorry, the book '{book_name}' is not available."

# Example Usage
store = BookStore()
book_name = input("Enter the book name you want to order: ").strip().lower()
print(store.order_book(book_name))
