def smallest(numbers):
    return min(numbers)

input_list = []
while True:
    command = input("Input a number or done. ")
    if command == "done":
        break
    try:
        input_list.append(int(command))
    except:
        print("Please input a number or 'done' to finish.")

minimum = smallest(input_list)
print(f"{minimum} is the smallest number.")