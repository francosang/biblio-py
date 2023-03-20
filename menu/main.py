import menu.authors
import menu.books
from globals import author_repository

author_repository.find_by_name("lol")

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
            case "Q" | "q" | "3":
                exit(0)