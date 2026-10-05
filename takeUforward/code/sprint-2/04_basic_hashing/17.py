# Highest Occurring Character
# Given a string `s`, find and return the character that appears the most times. If there is a tie, return the lexicographically smaller character.
#
# Example 1:
# Input: s = 'takeuforward'
# Output: 'a'  # Frequency is 2 (ties with 'r', 'a' is lexicographically smaller)
#
# Example 2:
# Input: s = 'success'
# Output: 's'  # Frequency is 3
#
# Example 3 (Edge Case - All Unique Characters):
# Input: s = 'dcba'
# Output: 'a'  # All have freq 1, 'a' is lexicographically smallest

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

freq = {}
for char in s : 
    freq[char] = freq.get(char, 0) + 1 

highest_frequency = -1
highest_char = ''

for char , count in freq.items() : 
    if count > highest_frequency : 
        highest_frequency = count 
        highest_char = char 
    elif count == highest_frequency : 
        if highest_char == '' or char < highest_char : 
            highest_char = char



print(f"The highest occurring character is : '{highest_char}'")
