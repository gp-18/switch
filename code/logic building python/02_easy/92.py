# Print all factors of a given number.

if (number := int(input("Enter the number: "))) >= 1:

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

else:
    print("Give a correct number")