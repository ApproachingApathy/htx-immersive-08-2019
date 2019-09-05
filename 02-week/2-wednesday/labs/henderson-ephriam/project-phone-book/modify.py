import data
import search
import menu
def index_finder(phonebook, sub_list, sub_list_index):
    """Finds the index of a matching value from two lists. """
    return phonebook.index(sub_list[sub_list_index])

def change_phone_number(index):
    modified_entry_number = input("Enter the new number (555-555-5555): ")
    print(f"Is {modified_entry_number} correct? Y/N")
    confirmation = input(">> ")
    if menu.get_confirmation(confirmation) == True:
        #TODO: Add exception handler.

        data.container_phonebook[index]["number"] = modified_entry_number
        print("Entry Saved")
        menu.await_input()

def delete_entry(phonebook_index, msg):
    print(msg)
    print("Would you like to delete this entry? Y/N")
    confirmation = input(">> ")

    if menu.get_confirmation(confirmation) == True:

        data.container_phonebook.pop(phonebook_index)
        print("Entry Deleted.")
        menu.await_input()

def create_new_entry():
    print("Creating new entry.")
    new_entry_first_name = input("First Name: ")
    new_entry_last_name = input("Last Name: ")
    new_entry_number = input("Phone Number (555-555-5555): ")

    
    print("Is this correct? Y/N")
    print(f"Name: {new_entry_first_name} {new_entry_last_name}")
    print(f"Number {new_entry_number}")
    confirmation = input(">> ")
    if menu.get_confirmation(confirmation) == True:
        data.container_phonebook.append({"first_name":new_entry_first_name, "last_name":new_entry_last_name, "number":new_entry_number})
    else:
        print("Operation canceled")
        menu.await_input()

def modify_entry(will_delete=False):
    """Will modify or delete an entry. Pass True to delete. """
    print("Modifying existing entry.")
    list_modify_select = search.search_tool() #Will return a
    if len(list_modify_select) > 0: #If the list returns anything.
        
        menu.print_sub_list(list_modify_select, "Choose an entry to modify.")

        while True:
            entry_select_command = menu.get_option()
            if entry_select_command > len(list_modify_select) or entry_select_command < 0: #Is the user's choice in the range of the list.
                print("That value is out of range.")
            else:
                modified_data_index = index_finder(data.container_phonebook, list_modify_select, entry_select_command)
                if will_delete == False:
                    change_phone_number(modified_data_index)
                    break
                else:
                    delete_entry(modified_data_index, ("{first_name} {last_name}: {number}".format(**list_modify_select[entry_select_command])))
                    break

def modify_menu():       

    print("Choose an option.")
    print("1. Create a new Entry")
    print("2. Modify an existing Entry.")
    modify_command = menu.get_option()
    if modify_command == 1:
        create_new_entry()
    elif modify_command == 2:
        modify_entry()




    #modify_list = search.search_tool()
