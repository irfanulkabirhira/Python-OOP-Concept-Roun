class Library:
    Book =['Hira', 'Jira']
    def __init__(self, Book_name, pages):
        self.Book_name =Book_name
        self.pages=pages
        if self.Book_name in Library.Book:
            print(f"The {self.Book_name} is available in the List")
        else:
            print(f"Sorry ! This {self.Book_name} is not Available in the List")

    def show(self):
        print(f"Book name : {self.Book_name}\nPages : {self.pages}")

print("-----Welcome to the Library ---------")
Book1 =Library('Hira', 27)
Book1.show()
