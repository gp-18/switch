# Take 24-hour time (hours and minutes) and print whether it is AM or PM.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

hours = int(input("Enter hours (0-23): "))
minutes = int(input("Enter minutes (0-59): "))

if 0 <= hours <= 23 and 0 <= minutes <= 59:
    if hours < 12:
        print("AM")
    else:
        print("PM")
else:
    print("Invalid time")
