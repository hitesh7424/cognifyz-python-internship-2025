"""
Task: Temperature Conversion
Create a Python program that converts temperatures between Celsius and Fahrenheit.
Prompt the user to enter a temperature value and the unit of measurement, and then
display the converted temperature.

Celsius to Fahrenheit

Fahrenheit to Celsius

C = (F - 32) * 5/9
F = C * 9/5 + 32

"""

# Prompt the user for input (e.g., "100 C" or "212 F")
temp_input = input()

# Split the input into value and unit
temp_value = float(temp_input.split()[0])
temp_unit = temp_input.split()[1]

# Function to convert temperature between Celsius and Fahrenheit
def temp_conversion(temp_value, temp_unit):
    if temp_unit.lower() == "f":
        temp_value = C = (temp_value - 32) * 5 / 9
        temp_unit = "C"
        # print(f"{temp_value:.2f} °{temp_unit}")
    elif temp_unit.lower() == "c":
        temp_value = temp_value * 9 / 5 + 32
        temp_unit = "F"
        # print(f"{temp_value:.2f} °{temp_unit}")
    else:
        print("Invalid unit.")
        
    return temp_value, temp_unit

# Call the conversion function
temp_converted = temp_conversion(temp_value, temp_unit)

# Display the result
print(temp_converted[0], temp_converted[1])
