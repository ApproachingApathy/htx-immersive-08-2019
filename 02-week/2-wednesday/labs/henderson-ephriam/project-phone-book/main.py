import data
import menu
import search
import modify
import list
while True:
    menu.main_menu()
    command = menu.get_option()

    if command == 1:
        search.search_tool(True)
    elif command == 2:
        modify.modify_menu()
    elif command == 3:
        modify.modify_entry(True)
    elif command == 4:
        list.list_all()
    elif command == 5:
        exit(0)
