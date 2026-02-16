from biblioteca.repository import InMemoryRepository
from biblioteca.servise import LibraryService
from biblioteca.exceptions import (
    BookAlreadyLoaned,
    UserLoanLimitReached,
    BookNotFound,
    UserNotFound
)


def run_tests():
    print("Iniciando pruebas...\n")

    repo = InMemoryRepository()
    service = LibraryService(repo)

    # agregar libro
    book = service.add_book("1984", "Orwell")
    assert book.title == "1984"
    print("agregar libro")

    # registrar usuario
    user = service.register_user("Samuel")
    assert user.name == "Samuel"
    print("registrar usuario")

    # préstamo
    service.loan_book(book.id, user.id)
    assert book.loaned_to == user.id
    print("préstamo")

    # no prestar libro ya prestado
    try:
        service.loan_book(book.id, user.id)
        assert False, "El libro no debería prestarse dos veces"
    except BookAlreadyLoaned:
        print("excepción libro ya prestado")

    # 5️⃣ devolución correcta
    service.return_book(book.id)
    assert book.loaned_to is None
    print("devolución correcta")

    # 6️⃣ límite de préstamos
    service = LibraryService(repo, max_loans_per_user=1)

    book1 = service.add_book("A", "Autor A")
    book2 = service.add_book("B", "Autor B")
    user2 = service.register_user("Ana")

    service.loan_book(book1.id, user2.id)

    try:
        service.loan_book(book2.id, user2.id)
        assert False, "El usuario no debería poder superar el límite"
    except UserLoanLimitReached:
        print("límite de préstamo")

    print("\nsi sirve")


if __name__ == "__main__":
    run_tests()