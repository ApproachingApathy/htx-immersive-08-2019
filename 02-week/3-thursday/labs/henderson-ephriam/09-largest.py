def largest(numbers):
    return max(numbers)

input_list = []
while True:
    command = input("Input a number or done. ")
    if command == "done":
        break
    try:
        input_list.append(int(command))
    except:
        print("Please input a number or 'done' to finish.")

maximum = largest(input_list)
print(f"{maximum} is the largest number.")