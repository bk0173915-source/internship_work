 

#Library Example (Single Inheritance)

class Books:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)


class IssuedBooks(Books):
    def __init__(self,title,author,issued_to,issued_date):
        self.issued_to=issued_to
        self.issued_date=issued_date
        super().__init__(title, author)

    def display_issued_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)
        print("The name of the person issued to is", self.issued_to)
        print("The date of issued is",self.issued_date)


IB=IssuedBooks("Python","John","Students","04-02-26")
IB.display_books_details()