# Solve a quadratic equation (handle real and complex roots).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:

    if b == 0:

        if c == 0:
            print("Infinite number of solutions")
        else:
            print("No solution")

    else:
        x = -c / b
        print("This is a linear equation")
        print("Root:", x)

else:

    discriminant = b * b - 4 * a * c

    if discriminant > 0:

        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)

        print("Two real roots:")
        print("Root 1:", root1)
        print("Root 2:", root2)

    elif discriminant == 0:

        root = -b / (2 * a)

        print("One repeated real root:")
        print("Root:", root)

    else:

        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

        print("Two complex roots:")
        print("Root 1:", root1)
        print("Root 2:", root2)
