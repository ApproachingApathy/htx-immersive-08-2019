def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5) + 32)

while True:
    try:
        celsius = int(input("Input a temperature in celsius. "))
        break
    except:
        print("Please input a number.")
print(celsius_to_fahrenheit(celsius))