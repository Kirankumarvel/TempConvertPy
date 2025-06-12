def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from user
celsius = float(input("Enter temperature in Celsius: "))

# Conversion
fahrenheit = celsius_to_fahrenheit(celsius)

# Output
print(f"{celsius}°C is equal to {fahrenheit}°F")
