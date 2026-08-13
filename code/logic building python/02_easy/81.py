# Check if a number is a palindrome.    

def reverse_number(number:int) :
    reverse = 0 

    while number > 0 : 
        last_digit = number % 10 
        reverse = reverse * 10 + last_digit
        number = number // 10 

    return reverse

def is_palindrome(number , reverse) :
    return True if number == reverse else False


if ( number:= int(input("Enter the number : "))) >= 0 :
    copy_number = number
    reverse = reverse_number(copy_number)
    print(is_palindrome(number = number , reverse=reverse))
else : 
    pass 