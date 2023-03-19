import menu.authors
import menu.books
from repository.author_repository import AuthorRepository

def show_main_menu():
    while True:
        print("+-------------------------------+")
        print("|           Main Menu           |")
        print("+-------------------------------+")
        print("Select an option\n")
        print("\tA) Manage Authors")
        print("\tB) Manage Books")    
        print("\tQ) Exit")    
        print("\nType an option > ")

        option = input()
        match option:
            case "A" | "a" | "1":
                menu.authors.show_authors_menu()
            case "B" | "b" | "2":
                menu.books.show_books_menu()
            case "Q" | "q":
                exit(0)