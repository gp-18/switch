# Count how many even digits a number contains.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("Enter the number: "))

number = abs(number)
count = 0

while number > 0:
    digit = number % 10

    if digit % 2 == 0:
        count += 1

    number //= 10

print("Even digits:", count)
