# Take a character and check if it's a vowel or consonant.
# Example 1: Input: 'a' -> Output: Vowel
# Example 2: Input: 'b' -> Output: Consonant

character = str(input("Enter the character : "))


print("vowel") if character in "aeiou" else print("consonant")
