def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return not is_even(x)

while True:
    try:
        number = int(input("Input a number. "))
        break
    except:
        print("Please input a number.")
if is_odd(number) == True:
    print(f"{number} is odd.")
else:
    print(f"{number} is not odd.")