# Convert a decimal number to binary, octal, and hexadecimal.
# Example 1: Input: 10 -> Output: 1010
# Example 2: Input: 5 -> Output: 101

number = int(input("Enter the decimal number: "))

if number >= 0:

    print("Binary:", bin(number))
    print("Octal:", oct(number))
    print("Hexadecimal:", hex(number))

else:
    print("Enter a valid non-negative number")
