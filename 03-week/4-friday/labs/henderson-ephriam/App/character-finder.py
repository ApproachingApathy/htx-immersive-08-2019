string_one = input("Input your first string.")
string_two = input("Input your second string.")
character_list = []

if string_one == string_two:
    print("These strings are the same!")
else:
    for value in string_two:
        if value not in string_one:
            character_list.append(value)


print(character_list)