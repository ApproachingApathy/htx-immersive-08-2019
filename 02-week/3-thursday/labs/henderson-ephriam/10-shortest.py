def smallest(strings):
    smallest_str = strings[0]
    for string in strings:
        if len(string) < len(smallest_str):
            smallest_str = string   
    return smallest_str

input_list = []
while True:
    command = input("Input a string or 0 to finish. ")
    if command == "0":
        break
    
    input_list.append(command)


minimum = smallest(input_list)
print(f"{minimum} is the shortest string.")