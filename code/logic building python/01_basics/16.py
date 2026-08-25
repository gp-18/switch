# Take a weekday number (1–7) and determine if it is a weekday or weekend.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("enter the number : "))


print("weekdays") if number in range(1,6) else print("weekend")
