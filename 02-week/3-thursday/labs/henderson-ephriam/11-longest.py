def largest(strings):
    largest_str = strings[0]
    for string in strings:
        if len(string) > len(largest_str):
            largest_str = string   
    return largest_str

input_list = []
while True:
    command = input("Input a string or 0 to finish. ")
    if command == "0":
        break
    
    input_list.append(command)


maximum = largest(input_list)
print(f"{maximum} is the longest string.")