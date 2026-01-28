# 2. Write a python program using function to convert Celsius to Fahrenheite.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"Temperature in Fahrenheit: {f}")
