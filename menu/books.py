def show_books_menu():
    while True:
        print("+-------------------------------+")
        print("|          Books Menu           |")
        print("+-------------------------------+")
        print("Select an option\n")
        print("\tV) View details")    
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
