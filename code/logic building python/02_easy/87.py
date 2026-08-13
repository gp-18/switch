# Print Fibonacci series up to n terms.

if (number := int(input("Enter the number: "))) >= 1:

    a = 0
    b = 1

    for i in range(number):
        print(a)
        a, b = b, a + b

else:
    print("Enter a valid number")

