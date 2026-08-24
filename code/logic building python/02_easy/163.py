# Count how many students passed.

if (number := int(input("Enter the number of students: "))) >= 1:

    passed = 0

    for i in range(number):
        marks = int(input(f"Enter marks of student {i + 1}: "))

        if marks >= 40:
            passed += 1

    print("Number of students passed:", passed)

else:
    print("Enter a valid number of students")