# Check whether a string is a palindrome.


if (string := input("Enter the string: ")) and len(string) >= 1:

    low = 0 
    high = len(string) - 1 
    is_palindrome = True

    while low < high : 

        if string[low] != string[high] :
            is_palindrome = False
            break 

        low = low + 1 
        high = high - 1 

    print("yes") if is_palindrome else print("no")

else:
    print("Enter a valid string")