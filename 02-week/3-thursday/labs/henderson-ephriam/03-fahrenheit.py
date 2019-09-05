def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

while True:
    try:
        fahrenheit = int(input("Input a temperature in fahrenheit. "))
        break
    except:
        print("Please input a number.")
print(fahrenheit_to_celsius(fahrenheit))