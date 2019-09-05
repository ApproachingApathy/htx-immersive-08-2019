import data
def list_all():
    """Lists all Entries. """
    for entry in data.container_phonebook:
        print("{first_name} {last_name}: {number}".format(**entry))