# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if ( number := int(input("Enter the number : "))) >= 0 : 
    if number % 100 == 0 and number % 500 == 0 and number % 2000 == 0 : 
        print("yes its evenly divided")
