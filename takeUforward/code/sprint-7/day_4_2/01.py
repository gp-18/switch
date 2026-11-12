# Roman to Integer
# Given a valid Roman numeral string s in the range [1, 3999],
# convert it to an integer.
# Symbols: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
# Subtractive combinations occur when a smaller symbol precedes a larger one.
#
# Example 1:
# Input:  s = "III"
# Output: 3
#
# Example 2:
# Input:  s = "XLII"
# Output: 42
# Explanation: XL (50 - 10 = 40) + II (2) = 42.
#
# Example 3:
# Input:  s = "MCMXCIV"
# Output: 1994
#
# Think About:
# - Store symbol values in a constant dictionary mp.
# - Traverse left to right comparing current symbol with next symbol.
# - If mp[s[i]] < mp[s[i + 1]]: subtract mp[s[i]] (subtractive pair).
# - Otherwise: add mp[s[i]] to total.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

s = input("Enter a valid Roman numeral string : ").strip().upper()

print(f"Your Roman numeral : '{s}'")

# Write your solution below:
# Optimal Approach: Single Pass with Lookahead Subtraction Rule
# Time Complexity: O(N) | Space Complexity: O(1)

def roman_to_int(roman_str):
    mp = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(roman_str)

    for i in range(n):
        # If current symbol is smaller than the next symbol, subtract it
        if i + 1 < n and mp[roman_str[i]] < mp[roman_str[i + 1]]:
            total -= mp[roman_str[i]]
        else:
            total += mp[roman_str[i]]

    return total

ans = roman_to_int(s)

print(f"The integer value is : {ans}")
