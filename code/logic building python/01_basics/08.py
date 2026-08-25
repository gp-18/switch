# Take a temperature value and print 'Cold', 'Warm', or 'Hot' using range conditions.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

temperature = float(input("Enter the temperature: "))

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Warm")
else:
    print("Hot")
