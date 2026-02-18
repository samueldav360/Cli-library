from servise import LibraryService
from repository import InMemoryRepository
from exceptions import *


def run_cli():

    repo = InMemoryRepository()
    service = LibraryService(repo)

    while True:
        print("\n--- LIBRARY CLI ---")
        print("1) Add book")
        print("2) List books")
        print("3) Register user")
        print("4) Loan book")
        print("5) Return book")
        print("6) List active loans")
        print("0) Exit")

        option = input("Choose option: ")

        try:

          
            if option == "1":
                title = input("Title: ")
                author = input("Author: ")
                b = service.add_book(title, author)
                print(f"Book added with id {b.id}")

        
            elif option == "2":
                books = service.list_books()
                if not books:
                    print("No books")
                for b in books:
                    status = "LOANED" if b.loaned_to else "AVAILABLE"
                    print(f"{b.id} | {b.title} | {b.author} | {status}")

            
            elif option == "3":
                name = input("User name: ")
                u = service.register_user(name)
                print(f"User registered with id {u.id}")

           
            elif option == "4":
                book_id = int(input("Book id: "))
                user_id = int(input("User id: "))
                service.loan_book(book_id, user_id)
                print("Loan created")

 
            elif option == "5":
                book_id = int(input("Book id: "))
                service.return_book(book_id)
                print("Book returned")

            
            elif option == "6":
                loans = service.list_active_loans()
                if not loans:
                    print("No active loans")
                for l in loans:
                    print(f"Book {l.book_id} → User {l.user_id}")

          
            elif option == "0":
                print("Bye")
                break

            else:
                print("Invalid option")

        

        except BookNotFound:
            print("Error: Book not found")

        except UserNotFound:
            print("Error: User not found")

        except BookAlreadyLoaned:
            print("Error: Book already loaned")

        except UserLoanLimitReached:
            print("Error: User reached loan limit")

        except ValueError:
            print("Error: invalid number")
