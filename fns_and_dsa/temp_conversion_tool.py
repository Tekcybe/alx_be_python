FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}\u00b0C is {converted}\u00b0F")
elif unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"{temperature}\u00b0F is {converted}\u00b0C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
