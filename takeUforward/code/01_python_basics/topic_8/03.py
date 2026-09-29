# Read three numbers and print the largest; handle ties.

# Example 1:
# Input: 10, 25, 25
# Output: Largest: 25 (tie between second and third)

# Example 2:
# Input: 7, 7, 7
# Output: All numbers are equal: 7

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

a_val = int(a) if a.is_integer() else a
b_val = int(b) if b.is_integer() else b
c_val = int(c) if c.is_integer() else c

if a == b == c:
    print(f"All numbers are equal: {a_val}")
elif a == b and a > c:
    print(f"Largest: {a_val} (tie between first and second)")
elif a == c and a > b:
    print(f"Largest: {a_val} (tie between first and third)")
elif b == c and b > a:
    print(f"Largest: {b_val} (tie between second and third)")
else:
    if a > b and a > c:
        largest = a_val
    elif b > a and b > c:
        largest = b_val
    else:
        largest = c_val
    print(f"Largest: {largest}")
