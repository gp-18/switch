# Check if a number is an Armstrong number.

def count_digits(number: int) -> int:
    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count


def find_armstrong(number: int, digit_count: int) -> int:
    answer = 0

    while number > 0:
        last_digit = number % 10
        answer = answer + last_digit ** digit_count
        number = number // 10

    return answer


def check_armstrong(armstrong_number: int, number: int) -> bool:
    return armstrong_number == number


if (number := int(input("Enter the number: "))) >= 0:

    digit_count = count_digits(number)

    copy_number = number
    armstrong_number = find_armstrong(copy_number, digit_count)

    print(check_armstrong(armstrong_number, number))

else:
    print("Enter a valid number")