# Find the smallest and largest digit in a given number.

if (number := int(input("Enter the number: "))) >= 1:
    smallest = float("inf")
    largest = float("-inf")

    while number > 0:
        last_digit = number % 10

        if last_digit > largest:
            largest = last_digit

        if last_digit < smallest:
            smallest = last_digit

        number = number // 10

    print("Smallest digit:", smallest)
    print("Largest digit:", largest)

else:
    print("Enter a valid number")