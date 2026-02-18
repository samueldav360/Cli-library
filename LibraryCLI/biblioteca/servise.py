from exceptions import *
from models import Loan


class LibraryService:

    def __init__(self, repo, max_loans_per_user=2):
        self.repo = repo
        self.max_loans = max_loans_per_user

    def add_book(self, title, author):
        return self.repo.add_book(title, author)

    def register_user(self, name):
        return self.repo.register(name)

    def loan_book(self, book_id, user_id):

        if book_id not in self.repo.books:
            raise BookNotFound()

        if user_id not in self.repo.users:
            raise UserNotFound()

        book = self.repo.books[book_id]

        if book.loaned_to is not None:
            raise BookAlreadyLoaned()
        count = 0
        for loan in self.repo.loans.values():
            if loan.user_id == user_id:
                count += 1

        if count >= self.max_loans:
            raise UserLoanLimitReached()

        book.loaned_to = user_id
        self.repo.loans[book_id] = Loan(book_id, user_id)

    def return_book(self, book_id):

        if book_id not in self.repo.books:
            raise BookNotFound()

        book = self.repo.books[book_id]
        book.loaned_to = None

        if book_id in self.repo.loans:
            del self.repo.loans[book_id]

    def list_books(self):
        return list(self.repo.books.values())

    def list_active_loans(self):
        return list(self.repo.loans.values())
