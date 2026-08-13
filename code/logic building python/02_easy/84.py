# Check if a number is a perfect number.
def perfect_square(number:int) -> bool : 
    number_sum = 0 

    for i in range(1,number) :
        if number % i == 0 : 
            number_sum = number_sum + i  

    return True if number_sum == number else False

if(number := int(input("Enter the number : "))) > 0 :
    print(perfect_square(number=number))
else : 
    print("Enter the correct number") 