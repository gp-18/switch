# Find the HCF (GCD) of two numbers.
# Example 1: Input: 12, 18 -> Output: 6
# Example 2: Input: 8, 20 -> Output: 4

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

hcf = 1

for i in range(2, min(number1, number2) + 1):

    if number1 % i == 0 and number2 % i == 0:
        hcf = i

print(hcf)
