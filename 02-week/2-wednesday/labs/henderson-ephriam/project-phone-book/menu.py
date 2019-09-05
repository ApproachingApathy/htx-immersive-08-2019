def get_option():
    while True:
        try:
            option = int(input(">> "))
            return option
        except:
            print("Please enter a valid option.")

def get_confirmation(str):
    """Returns True is Yes, False if str is No. """
    str = str.lower()
    loop_counter = 0
    while True:
        if str == "yes" or str == "y":
            return True
        elif str == "no" or str == "n":
            return False
        else:
            if loop_counter > 2:
                print("Cancelling Operation.")
                return False
                break
            print("Please enter yes or no")
            str = input(">> ")
            loop_counter += 1
        

def main_menu():
    print("============================")
    print("Phone Book")
    print("============================")

    print("Select an option from the list below.")
    print("1. Look up an entry")
    print("2. Create or change an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")




