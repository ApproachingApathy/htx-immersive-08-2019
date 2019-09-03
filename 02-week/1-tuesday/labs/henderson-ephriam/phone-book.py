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

    else:
        print("Input a valid command")





