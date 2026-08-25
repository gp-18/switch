# Return the integer mean of all digits of a number.
# Example 1: Input: 512 -> Output: 2 ((5+1+2)//3)
# Example 2: Input: 666 -> Output: 6

num_str = input("Enter a number: ")

digits = [int(d) for d in num_str if d.isdigit()]
if digits:
    mean_val = sum(digits) // len(digits)
    print("Integer mean of digits:", mean_val)
else:
    print("No valid digits found")
