import data
import search
import menu
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





def modify_entry(will_delete=False):
    print("Modifying existing entry.")
    list_modify_select = search.search_tool() #Will return a
    if len(list_modify_select) > 0: #If the list returns anything.
        
        print("Please choose an entry to modify:")
        
        for entry in list_modify_select: #Print each list item with it's index.
            print(str(list_modify_select.index(entry)) + ". {first_name} {last_name}: {number}".format(**entry))
        
        while True:
            entry_select_command = menu.get_option()
            if entry_select_command > len(list_modify_select) or entry_select_command < 0: #Is the user's choice in the range of the list.
                print("That value is out of range.")
            else:
                if will_delete == False:
                    modified_entry_number = input("Enter the new number (555-555-5555): ")
                    print(f"Is {modified_entry_number} correct? Y/N")
                    confirmation = input(">> ")
                    if menu.get_confirmation(confirmation) == True:
                        #TODO: Add exception handler.
                        modified_data_index = data.container_phonebook.index(list_modify_select[entry_select_command]) #Searches the phone book for the entry and returns the index.

                        data.container_phonebook[modified_data_index]["number"] = modified_entry_number
                        print("Entry Saved")
                        break
                    else:
                        break
                else:
                    print("{first_name} {last_name}: {number}".format(**list_modify_select[entry_select_command]) )
                    print("Would you like to delete this entry? Y/N")
                    confirmation = input(">> ")

                    if menu.get_confirmation(confirmation) == True:
                        modified_data_index = data.container_phonebook.index(list_modify_select[entry_select_command])
                        data.container_phonebook.pop(modified_data_index)
                        print("Entry Deleted.")
                        break
                    else:
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
