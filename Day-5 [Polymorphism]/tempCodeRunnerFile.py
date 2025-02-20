class Book:
    def _init_(self, title, page):
        self.title = title
        self.page = page

    def details(self):
        print(self.title)
        print(self.page)

    def _add_(self,other):
        total = self.page + other.page
        return Book('all book', total)

    def _str_(self):
        return str(self.page)


b1 = Book('A',10)
b2 = Book('B',20)
b3 = Book('C',10)

print("Total no of pages: ",b1+b2+b3)