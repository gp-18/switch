# Build a calculator that prints sum, difference, product, quotient, floor quotient, and remainder for two numbers; handle division by zero.

# Example 1:
# Input: a = 10, b = 3
# Output: Sum: 13, Diff: 7, Prod: 30, Quot: 3.3333333333333335, Floor: 3, Rem: 1

# Example 2:
# Input: a = 10, b = 0
# Output: Sum: 10, Diff: 10, Prod: 0, Cannot divide by zero!

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
# Calculate sum, difference, and product
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b 
# Print sum, difference, and product
print(f"Sum: {sum_ab}, Diff: {diff_ab}, Prod: {prod_ab}", end=', ')
# Handle division by zero for quotient, floor quotient, and remainder   
if b != 0:
    quot_ab = a / b
    floor_ab = a // b
    rem_ab = a % b
    # Print quotient, floor quotient, and remainder
    print(f"Quot: {quot_ab}, Floor: {floor_ab}, Rem: {rem_ab}")
else:
    print("Cannot divide by zero!")