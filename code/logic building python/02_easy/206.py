# Find the sum of numbers evenly divisible by c in range a to b.
# Example 1: Input: a=1, b=10, c=3 -> Output: 18 (3+6+9)
# Example 2: Input: a=1, b=10, c=2 -> Output: 30 (2+4+6+8+10)

a = int(input("Enter start range a: "))
b = int(input("Enter end range b: "))
c = int(input("Enter divisor c: "))

if c != 0:
    total_sum = sum(i for i in range(a, b + 1) if i % c == 0)
    print(f"Sum of numbers divisible by {c}:", total_sum)
else:
    print("Divisor cannot be zero")
