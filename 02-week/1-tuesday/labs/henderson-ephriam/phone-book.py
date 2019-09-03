#ApathyWorks



option = 0
phonebook_dict = {
    "John Doe": "555-555-0001",
    "Jane Doe": "555-555-0002",
    "Joe Schmoe": "555-555-0003",
    "Nancy Wheeler": "555-555-5277",
    "Johnathon Byers": "555-555-4433",
    "Demo": "555-555-4355"
}


print("Phone book")
print("=============")
while True:
    print("Phone book")
    print("=============")
    print("1. Look up an entry")
    print("2. Create or change an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")
    while True:
        try:
            option = int(input(">> "))
            break
        except:
            print("Input a valid command")
    if option == 1:
        locator = input("Enter a name: ").lower()
        
        is_entry_found = False
        for key in phonebook_dict:
            if key.lower() == locator:
                print(f"{key}: {phonebook_dict[key]}")
                is_entry_found = True
        if is_entry_found == False:
            print("No entries found.")

        print("Search Complete")
    elif option == 2:
        new_contact = input("Input a name: ")
        new_number = input("Input a number (555-555-5555): ")

        answer = input(f"Is {new_contact}: {new_number} correct? Y/N ").lower()
        while True:
            if answer == "y":
                phonebook_dict[new_contact] = new_number
                print("Contact Saved.")
                break
            elif answer == "n":
                print("Contact not saved")
            else:
                answer = input("Input Y/N ")
    elif option == 3:
        marked_contact = input("Enter a name for deletion: ").lower()
        is_entry_found = False
        for key in phonebook_dict:
            if key.lower() == marked_contact:
                is_entry_found = True
                answer = input(f"Would you like to delete {key}? Y/N ").lower()
                if answer == "y":
                    del phonebook_dict[key]
                    print("Contact Deleted")
                elif answer == "n":
                    print("Contact not Deleted.")
                else:
                    answer = input("Input Y/N ")
            if is_entry_found == False:
                print("No entries found.")
    elif option == 4:
        for key in phonebook_dict:
            print(f"{key}: {phonebook_dict[key]}")
    elif option == 5:
        exit(0)
    else:
        print("Input a valid command")





