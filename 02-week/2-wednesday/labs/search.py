import data
def search_tool():
    search_term = input("Search for: ").lower()
    is_item_found = False

    for entry in data.container_phonebook: #Search for each dictionary in the list.
        for key in entry: #Search for each key in the dictionary.
            if entry[key].lower() == search_term: #Search each value in the dictionary.
                
                print("{first_name} {last_name}: {number}".format(**entry)) #** is an operator that unpacks a dictionary.
                is_item_found = True
    if is_item_found != True:
        print("No Entries Found")
    
            

