# ai bar Library er Daitte achi ==> So ami book push korbo Library er list e
class Library:
    Book=['hira']
    def __init__(self,Book_name , pages):
        self.Book_name =Book_name
        self.pages=pages
        if self.Book_name not in Library.Book:
            self.Book.append(Book_name)
        else:
            print (f"This {self.Book_name} is Already In the List")
    def show(self):
        print(f"Book name : {self.Book_name}\nPages : {self.pages}\nBook list is : {Library.Book}")

print("------Welcome to the Library------------")
obj=Library('hira',23)
obj1=Library('Hala', 23)
obj2=Library('Mira',23)
#Printing the Obj1 Book
obj1.show()