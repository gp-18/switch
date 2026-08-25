# Take age inputs and count how many are adults, minors, and seniors.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number of people: "))) >= 1:

    minors = 0
    adults = 0
    seniors = 0

    for i in range(number):

        age = int(input(f"Enter age of person {i + 1}: "))

        if age < 18:
            minors += 1

        elif age < 60:
            adults += 1

        else:
            seniors += 1

    print("Minors:", minors)
    print("Adults:", adults)
    print("Seniors:", seniors)

else:
    print("Enter a valid number")
