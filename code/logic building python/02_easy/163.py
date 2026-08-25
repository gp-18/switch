# Given marks of students, find how many passed (>= 40).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number of students: "))) >= 1:

    passed = 0

    for i in range(number):
        marks = int(input(f"Enter marks of student {i + 1}: "))

        if marks >= 40:
            passed += 1

    print("Number of students passed:", passed)

else:
    print("Enter a valid number of students")
