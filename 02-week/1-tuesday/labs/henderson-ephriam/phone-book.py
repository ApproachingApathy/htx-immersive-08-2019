#ApathyWorks



option = 0
phonebook_dict = {
    "John Doe": "555-555-0001",
    "Jane Doe": "555-555-0002",
    "Joe Schmoe": "555-555-0003",
    "Nancy Wheeler": "555-555-5277",
    "Jonathon Byers": "555-555-4433",
    "Demo": "555-555-4355"
}

#Main Menu
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

    #This While loop gets user input.
    while True:
        try:
            option = int(input(">> "))
            break
        except:
            print("Input a valid command")

    #This if statement evaluates user input
    if option == 1:
        locator = input("Enter a name: ").lower() #Get a name to search and make it lowercase. I make it lowercase so that the user can type the search term in any case they wish.
        
        is_entry_found = False
        for key in phonebook_dict: #This for loop searches each entry for the user's input.
            if key.lower() == locator: #I also make key(name) lowercase.
                print(f"{key}: {phonebook_dict[key]}")
                is_entry_found = True #Tells me if anything was was found.
        if is_entry_found == False: 
            print("No entries found.")

        print("Search Complete")
    elif option == 2:
        new_contact = input("Input a name: ")
        new_number = input("Input a number (555-555-5555): ")

        answer = input(f"Is {new_contact}: {new_number} correct? Y/N ").lower() #Gets user input to confirm changes.
        #A potential improvement is to verify if the user is overwriting an entry.
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
        marked_contact = input("Enter a name for deletion: ").lower() #Get user input for contact to delete.
        is_entry_found = False
        for key in phonebook_dict:
            if key.lower() == marked_contact: #If the user input is in the phone book.
                is_entry_found = True
                answer = input(f"Would you like to delete {key}? Y/N ").lower() #Get user confirmation.
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





