def get_option():
    while True:
        try:
            option = int(input(">> "))
            return option
        except:
            print("Please enter a valid option from 1-5.")

def main_menu():
    print("============================")
    print("Phone Book")
    print("============================")

    print("Input an option from the list below.")
    print("1. Look up an entry")
    print("2. Create or change an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")




