# Validate if three integers form a Pythagorean triplet.
# Example 1: Input: 3, 4, 5 -> Output: Pythagorean triplet (3^2 + 4^2 = 5^2)
# Example 2: Input: 5, 6, 7 -> Output: Not a Pythagorean triplet

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")
