from model.author import Author
from globals import author_repository

def show_authors_menu():
    while True:
        print("+-------------------------------+")
        print("|         Authors Menu          |")
        print("+-------------------------------+")
        print("Select an option\n")
        print("\tV) View")    
        print("\tF) Find")    
        print("\tA) Add")    
        print("\tE) Edit")    
        print("\tD) Delete") 
        print("\tL) List all")
        print("\tB) Back")
        print("\nType an option > ")

        option = input()
        match option:
            case "V" | "v" | "1":
                show_view_author()            
            case "F" | "f" | "2":
                show_find_author()
            case "A" | "a" | "3":
                show_add_author()
            case "E" | "e" | "4":
                show_edit_author(None)
            case "D" | "d" | "5":
                show_delete_author(None)
            case "L" | "l" | "6":
                show_list_authors()
            case "B" | "b" | "7":
                break
            case "Q" | "q":
                exit(0)

def show_view_author():
    print("+-------------------------------+")
    print("|          View Author         |")
    print("+-------------------------------+")

    int("caca")
    while True:
        try:
            id = int(input("Enter the Author's id to view: "))
            show_details(id)
            return
        except Exception as e:
            print(e)
            print("The id should be a number")


def show_list_authors():
    print("+-------------------------------+")
    print("|          List Authors         |")
    print("+-------------------------------+")

    authors = author_repository.get_list()

    print(f"---- Results: {len(authors)} ----")

    for a in authors:
        print(f'\t{a.id} - {a.name}')

    print("")
    print("Options:")
    print("\tPress Intro to go back")
    print("\tEnter ID to see details >")
    
    value = input("")

    try: 
        id = int(value)
        show_details(id)
    except Exception as e:
        pass

def show_find_author():
    print("+-------------------------------+")
    print("|          Find Author          |")
    print("+-------------------------------+")

    name = input("Name > ")

    authors = author_repository.find_by_name(name)

    print(f"---- Results: {len(authors)} ----")

    for a in authors:
        print(f'\t{a.id} - {a.name}')

    print("")
    print("Options:")
    print("\tPress Intro to go back")
    print("\tEnter ID to see details >")
    
    value = input()

    try: 
        id = int(value)
        show_details(id)
    except Exception as e:
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
    print("\tD) Delete")    
    print("\tB) Back")
    print("\nType an option > ")

    option = input()
    match option:
        case "E" | "e" | "1":
            show_edit_author(id)
        case "D" | "d" | "2":
            show_delete_author(id)
        case "Q" | "q":
            exit(0)

def show_delete_author(id: int | None):
    print("+-------------------------------+")
    print("|         Delete Author         |")
    print("+-------------------------------+")

    if id == None:
        while True:
            try:
                id = int(input(f"Enter the Author's id to delete: "))
                print("")
                break
            except:
                print("The id should be a number")

    a = author_repository.get_by_id(id)

    print(f"Name: {a.name}")
    print(f"Country: {a.country}")
    print(f"Born: {a.born}")
    print("")
    print("Confirm delete?")
    print("\tYes")
    print("\tPress enter to go back")

    option = input().lower()
    if option == "yes":
        author_repository.delete(id)

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
