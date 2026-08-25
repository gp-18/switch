# List numbers in range x to y divisible by n.
# Example 1: Input: x=1, y=10, n=2 -> Output: [2, 4, 6, 8, 10]
# Example 2: Input: x=1, y=20, n=5 -> Output: [5, 10, 15, 20]

x = int(input("Enter start x: "))
y = int(input("Enter end y: "))
n = int(input("Enter divisor n: "))

if n != 0:
    divisible_nums = [i for i in range(x, y + 1) if i % n == 0]
    print(f"Numbers divisible by {n}:", divisible_nums)
else:
    print("Divisor cannot be zero")
