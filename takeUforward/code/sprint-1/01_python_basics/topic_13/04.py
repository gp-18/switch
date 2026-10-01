# Reverse the digits of a non-negative integer using % and //.

# Example 1:
# Input: 1234
# Output: 4321

# Example 2:
# Input: 500
# Output: 5

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
elif number == 0:
    print("Reversed number: 0")
else:
    reversed_number = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10
    print(f"Reversed number: {reversed_number}")
