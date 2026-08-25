# Use a generator to print even numbers up to n in comma-separated form.
# Example 1: Input: 10 -> Output: 0,2,4,6,8,10
# Example 2: Input: 6 -> Output: 0,2,4,6

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("Enter n: "))
if n >= 0:
    print(",".join(even_generator(n)))
else:
    print("Please enter a non-negative integer")
