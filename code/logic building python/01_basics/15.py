# Take a single digit (0-9) and print its word form.

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