# Count how many even digits a number contains.

number = int(input("Enter the number: "))

number = abs(number)
count = 0

while number > 0:
    digit = number % 10

    if digit % 2 == 0:
        count += 1

    number //= 10

print("Even digits:", count)