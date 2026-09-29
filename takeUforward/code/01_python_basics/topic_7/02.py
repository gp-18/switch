# Check whether a number lies in the inclusive range 10 to 50.

# Example 1:
# Input: 25
# Output: 25 is within the range [10, 50]

# Example 2:
# Input: 5
# Output: 5 is outside the range [10, 50]

number = float(input("Enter a number: "))
num_val = int(number) if number.is_integer() else number

if 10 <= number <= 50:
    print(f"{num_val} is within the range [10, 50]")
else:
    print(f"{num_val} is outside the range [10, 50]")
