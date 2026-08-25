# Print Fibonacci series up to n terms.
# Example 1: Input: 5 -> Output: 0 1 1 2 3
# Example 2: Input: 3 -> Output: 0 1 1

if (number := int(input("Enter the number: "))) >= 1:

    a = 0
    b = 1

    for i in range(number):
        print(a)
        a, b = b, a + b

else:
    print("Enter a valid number")
