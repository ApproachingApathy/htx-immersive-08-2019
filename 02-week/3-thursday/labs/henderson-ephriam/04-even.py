def is_even(x):
    return x % 2 == 0

while True:
    try:
        number = int(input("Input a number. "))
        break
    except:
        print("Please input a number.")
if is_even(number) == True:
    print(f"{number} is even.")
else:
    print(f"{number} is not even.")
