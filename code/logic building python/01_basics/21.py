# Print the multiplication table of a given number (n × 1 to n × 10).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("Enter the number : "))


for i in range(1,11) :
  print(f"{number} x {i} = {number * i}")
