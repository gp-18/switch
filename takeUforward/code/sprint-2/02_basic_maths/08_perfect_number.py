# Perfect Number
# Check whether a number is equal to the sum of its proper divisors (excluding itself).
#
# Example 1:
# Input: n = 6
# Output: True  # Proper divisors: 1 + 2 + 3 = 6
#
# Example 2:
# Input: n = 28
# Output: True  # Proper divisors: 1 + 2 + 4 + 7 + 14 = 28
#
# Example 3 (Edge Case - Smallest Positive Integer):
# Input: n = 1
# Output: False  # Proper divisors sum is 0 != 1


number = int(input("Enter the number : "))

ans = 0 

for i in range(1,number) :
  
  if  number % i == 0 :
    ans += i
   
print("yes") if ans == number else print("no")


