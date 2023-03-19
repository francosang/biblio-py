def start():
    show_main_menu()

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
                show_authors_menu()
            case "B" | "b" | "2":
                ... 
            case "Q" | "q":
                exit(0)

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
    print("\nType an author's name > ")

def show_add_author():
    print("+-------------------------------+")
    print("|           Add Author          |")
    print("+-------------------------------+")
    print("\nIntroduce the author info:\n")

    name = input("Name > ")
    country = input("Country > ")
    born = input("Born date > ")
