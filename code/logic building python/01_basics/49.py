# Convert Celsius to Fahrenheit.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")
