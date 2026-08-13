# Print first n terms of an arithmetic progression.

a = int(input("Enter the first term (a): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

for i in range(n):
    print(a)
    a = a + d