
class Book:
    id = 1
    def __init__(self):
        self.title = None
        self.author = None
        self._loan_status = None
        self._lender = None

    def add(self, title, author):
        self.title = title
        self.author = author
        self.id = Book.id
        Book.id += 1

class User:
    id = 1
    def __init__(self,):
        self.name = None

    def add(self, name):
        self.name = name
        self.id = User.id
        User.id += 1

class Loan:
    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id