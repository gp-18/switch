# Take 5 numbers as input; skip zeros using continue,
# then print the sum of all non-zero numbers.

total = 0

for i in range(5):
    number = int(input("Enter the number: "))

    if number == 0:
        continue

    total += number

print("Sum of non-zero numbers:", total)