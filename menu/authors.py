import sqlite3
from model.author import Author
from repository.author_repository import AuthorRepository

con = sqlite3.connect("biblo.db")
author_repository = AuthorRepository(con)

def show_authors_menu():
    while True:
        print("+-------------------------------+")
        print("|         Authors Menu          |")
        print("+-------------------------------+")
        print("Select an option\n")
        print("\tF) Find")    
        print("\tA) Add")    
        print("\tE) Edit")    
        print("\tD) Delete") 
        print("\tL) List all")
        print("\tB) Back")
        print("\nType an option > ")

        option = input()
        match option:
            case "F" | "f" | "1":
                show_find_author()
            case "A" | "a" | "2":
                show_add_author()
            case "B" | "b" | "3":
                break
            case "Q" | "q":
                exit(0)

def show_find_author():
    print("+-------------------------------+")
    print("|          Find Author          |")
    print("+-------------------------------+")

    name = input("Name > ")

    authors = author_repository.findByName(name)

    print(f"---- Results: {len(authors)} ----")

    for a in authors:
        print(a.name)
        print(f'\t{a.country}')
        print(f'\t{a.born}\n')
    
    name = input("Press Enter to continue...")


def show_add_author():
    print("+-------------------------------+")
    print("|           Add Author          |")
    print("+-------------------------------+")
    print("\nIntroduce the author info:\n")

    name = input("Name > ")
    country = input("Country > ")
    born = input("Born date > ")

    author = Author(name, country, born)

    author_repository.save(author)
