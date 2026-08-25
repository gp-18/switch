# Take a number and print 'Fizz' if divisible by 3, 'Buzz' if divisible by 5, and 'FizzBuzz' if divisible by both.
# Example 1: Input: 25 -> Output: divisible by 5
# Example 2: Input: 14 -> Output: not divisible by 5

if (number :=  int(input("Enter the number : "))) >= 0 : 
    if number % 3 == 0 and number % 5 == 0 : 
        print("FizzBuzz")
    elif number % 3 == 0 : 
        print("Fizz")
    elif number % 5 == 0 : 
        print("Buzz")
    else : 
        print("nothing")
else :
    print("enter the correct number")
