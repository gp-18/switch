# Print first n terms of a geometric progression.

a = int(input("Enter the first term (a): "))
r = int(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

for i in range(n):
    print(a)
    a = a * r