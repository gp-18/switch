# Create a new array containing squares of all elements.
if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    new_array = [ x * x  for x in array]
    print(new_array)
else:
    print("Enter the valid length")