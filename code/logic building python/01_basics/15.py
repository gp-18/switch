# Take a single digit (0–9) and print its word form ('Zero' to 'Nine').
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

def check_digit(number: int):
    digits = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    return digits.get(number, "Please enter a valid digit from 0 to 9")


number = int(input("Give me a digit: "))
print(check_digit(number))
