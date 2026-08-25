# Print first n terms of a geometric progression given first term a and common ratio r.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

a = int(input("Enter the first term (a): "))
r = int(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

for i in range(n):
    print(a)
    a = a * r
