import data
from menu import await_input
def search_tool(will_print=False):
    """If will_print is true will search for and print entries in the phonebook. If false it will return a list with those entries instead."""
    search_term = input("Search for: ").lower()
    is_item_found = False
    list_out = []

    for entry in data.container_phonebook: #Search for each dictionary in the list.
        for key in entry: #Search for each key in the dictionary.
            if entry[key].lower() == search_term: #Search each value in the dictionary.
                if will_print == True:
                    print("{first_name} {last_name}: {number}".format(**entry)) #** is an operator that unpacks a dictionary.
                    is_item_found = True
                else:
                    list_out.append(entry) 
        if ("{first_name} {last_name}".format(**entry)).lower() == search_term:
            print("{first_name} {last_name}: {number}".format(**entry)) #** is an operator that unpacks a dictionary.
            is_item_found = True

    if is_item_found == False:
        print("No Entries Found")
    await_input()
    return list_out
    
            

