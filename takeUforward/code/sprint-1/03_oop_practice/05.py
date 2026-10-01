# ============================================================
# Problem: Temperature Converter
# Difficulty: Easy
# ============================================================
#
# PROBLEM STATEMENT:
# Create a Temperature class with a Celsius value.
# Add methods to convert the temperature to Fahrenheit and Kelvin.
# Formulae:
# - Fahrenheit = (Celsius * 9/5) + 32
# - Kelvin = Celsius + 273.15
# Implement solution() returning conversions rounded to 2 decimal places.
#
# INPUT:
# - celsius: number
#
# OUTPUT:
# - String with Fahrenheit and Kelvin values:
#   "Fahrenheit: <val>\nKelvin: <val>"
#
# EXAMPLE:
# Input:  25
# Output: "Fahrenheit: 77.00\nKelvin: 298.15"
#
# CONSTRAINTS:
# - celsius >= -273.15 (Absolute zero)
# ============================================================

class Temperature:
    def __init__(self, celsius):
        pass

    def to_fahrenheit(self):
        pass

    def to_kelvin(self):
        pass

    def get_conversions(self):
        pass


def solution(celsius):
    # Create Temperature and return formatted conversions
    pass


# ---- TEST CASES ----
assert solution(25) == "Fahrenheit: 77.00\nKelvin: 298.15", "Test 1 Failed"
assert solution(0) == "Fahrenheit: 32.00\nKelvin: 273.15", "Test 2 Failed"
assert solution(100) == "Fahrenheit: 212.00\nKelvin: 373.15", "Test 3 Failed"
assert solution(-40) == "Fahrenheit: -40.00\nKelvin: 233.15", "Test 4 Failed"

print("All test cases passed!")
