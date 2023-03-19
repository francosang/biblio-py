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
            case "E" | "e" | "3":
                show_edit_author(None)
            case "B" | "b" | "4":
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
        print(f'\t{a.id} - {a.name}')
    
    value = input("Introduce an ID to see details or Enter to go back...")

    try: 
        id = int(value)
        show_details(id)
    except Exception as e:
        print(e)
        pass

def show_details(id):
    a = author_repository.get_by_id(id)

    print("+-------------------------------+")
    print("|         Author Details        |")
    print("+-------------------------------+")
    print("")
    print(f"Name: {a.name}")
    print(f"Country: {a.country}")
    print(f"Born date: {a.born}")
    print("")
    print("Select an option\n")
    print("\tE) Edit")    
    print("\tB) Back")
    print("\nType an option > ")

    option = input()
    match option:
        case "E" | "e" | "1":
            show_edit_author(id)
        case "Q" | "q":
            exit(0)

def show_edit_author(id: int | None):
    print("+-------------------------------+")
    print("|          Edit Author          |")
    print("+-------------------------------+")

    if id == None:
        while True:
            try:
                id = int(input(f"Enter the Author's id to edit: "))
                break
            except:
                print("The id should be a number")

    a = author_repository.get_by_id(id)


    print("")
    name = input(f"Name ({a.name}): ")
    country = input(f"Country ({a.country}): ")
    born = input(f"Born ({a.born}): ")

    name = name if name else a.name
    country = country if country else a.country
    born = born if born else a.born

    author = Author(name, country, born)
    author_repository.update(id, author)

def show_add_author():
    print("+-------------------------------+")
    print("|           Add Author          |")
    print("+-------------------------------+")
    print("\nIntroduce the author info:\n")

    name = input("Name > ")
    country = input("Country > ")
    born = input("Born date > ")

    author = Author(name, country, born)
    author_repository.insert(author)
