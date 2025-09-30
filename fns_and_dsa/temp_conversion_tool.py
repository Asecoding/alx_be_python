
# Global  conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0   # Factor to convert Celsius to Fahrenheit
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        # Try to convert input to float, raise error if invalid
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
