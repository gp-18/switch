# Check the temperature

temperature = float(input("Enter the temperature: "))

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Warm")
else:
    print("Hot")