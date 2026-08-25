# Find the sum of all factors of a number.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

if (number := int(input("Enter the number: "))) >= 1:
    sum = 0 

    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    print(sum)
else:
    print("Give a correct number")
