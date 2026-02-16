from models import Book, User, Loan
book = Book()
user = User()
loan = Loan()

class InMemoryRepository:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.loans = {}

    def add(self, title, author):
        book.add(title, author)
        self.books[book.id] = book.title, book.author
    def register(self, name):
        user.add(name)
    
    def lend(self, book, lender):
        pass
        
library = InMemoryRepository()
library.add("1989", "george orwell")