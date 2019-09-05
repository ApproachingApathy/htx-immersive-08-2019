def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return not is_even(x)

def only_evens(numbers):
    only_evens = []
    for number in numbers:
        if is_even(number) == True:
            only_evens.append(number)
    return only_evens

input_list = []
while True:
    command = input("Input a number or done. ")
    if command == "done":
        break
    try:
        input_list.append(int(command))
    except:
        print("Please input a number or 'done' to finish.")

out = only_evens(input_list)
out.sort()
print(out)