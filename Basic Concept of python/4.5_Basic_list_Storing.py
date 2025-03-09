class Library:
    Book =['Hira', 'Jira']
    def __init__(self, Book_Name, pages):
        self.Book_name =Book_Name
        self.pages=pages

        # Condition
        if self.Book_name in Library.Book:
            print(f"This {self.Book_name} is Available in the List")
        else:
            print(f"The Book is not available in the Book list")

book1=Library('Hira', 23)
