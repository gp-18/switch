# Find the sum of all factors of a number.

if (number := int(input("Enter the number: "))) >= 1:
    sum = 0 

    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    print(sum)
else:
    print("Give a correct number")