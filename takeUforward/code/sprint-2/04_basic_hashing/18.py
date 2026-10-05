# Lowest Occurring Character
# Given a string `s`, find and return the character that appears the least number of times (lowest frequency). If multiple have the same lowest frequency, return the lexicographically smaller character.
#
# Example 1:
# Input: s = 'banana'
# Output: 'b'  # 'b' has frequency 1
#
# Example 2:
# Input: s = 'aabbcc'
# Output: 'a'  # All have frequency 2, 'a' is lexicographically smallest
#
# Example 3 (Edge Case - Mixed Case Sensitivity):
# Input: s = 'zZ'
# Output: 'Z'  # In ASCII, 'Z' (90) is smaller than 'z' (122)

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")


freq = {}
for char in s : 
    freq[char] = freq.get(char, 0) + 1 

lowest_freq = float("inf")
lowest_char = ''

 
for char , count in freq.items() :
    if count < lowest_freq :
        lowest_freq = count 
        lowest_char = char 
    
    elif count == lowest_freq :
        if lowest_char == '' or ord(char) < ord(lowest_char) :
            lowest_char = char 


print(f"The lowest occurring character is : '{lowest_char}'")