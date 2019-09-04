import data
import menu
import search

menu.main_menu()
command = menu.get_option()

if command == 1:
    search.search_tool()
