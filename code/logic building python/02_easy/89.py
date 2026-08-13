# Print all numbers between a and b divisible by 7.


a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)