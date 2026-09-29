# Convert a numeric score into grades using clearly stated grade boundaries; test exact boundary values.

# Example 1:
# Input: score = 85 (e.g. >=90: A, >=80: B, >=70: C, >=60: D, else: F)
# Output: Grade: B

# Example 2:
# Input: score = 60
# Output: Grade: D

# Grade boundaries:
# Score >= 90: A
# Score >= 80: B
# Score >= 70: C
# Score >= 60: D
# Score < 60:  F

score = float(input("Enter the score: "))

if score < 0 or score > 100:
    print("Invalid score! Please enter a value between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
