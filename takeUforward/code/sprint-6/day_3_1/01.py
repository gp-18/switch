# Koko Eating Bananas
# A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas.
# An integer h represents the total time in hours to eat all the bananas.
# Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas.
# If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile
# and does not consume any more bananas in that hour.
# Determine the minimum number of bananas the monkey must eat per hour to finish
# all the bananas within h hours.
#
# Example 1:
# Input:  nums = [7, 15, 6, 3], h = 8
# Output: 5
# Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly.
# So, he will take 8 hours to complete all the piles.
#
# Example 2:
# Input:  nums = [25, 12, 8, 14, 19], h = 5
# Output: 25
# Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly.
# So, he will take 5 hours to complete all the piles.
#
# Example 3:
# Input:  nums = [3, 7, 6, 11], h = 8
# Output: 4
#
# Think About:
# - Search space: low = 1, high = max(nums).
# - As eating rate k increases, total hours needed monotonically decreases.
# - If total_hours <= h: mid is a valid rate, search left (high = mid - 1) to minimize.
# - Else: search right (low = mid + 1).
# - Ceiling division without floats: (banans + mid - 1) // mid.
# - Time Complexity: O(N * log(max(nums)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the number of piles (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter bananas in pile {i} : "))
    array.append(value)

h = int(input("Enter total hours available (h) : "))

print(f"Your piles : {array} with total hours h = {h}")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [1, max(nums)]
# Time Complexity: O(N * log(max(nums))) | Space Complexity: O(1)

low = 1 
high = max(array)
ans = high 

while low <= high: 

    mid = low + (high - low) // 2 

    total_hours = 0 

    for banans in array: 
        # -------------------------------------------------------------------------
        # EXPLANATION OF LOGIC: (banans + mid - 1) // mid
        # -------------------------------------------------------------------------
        # Goal: Calculate ceil(banans / mid) using pure integer arithmetic,
        # without converting to floating-point numbers (avoiding math.ceil).
        #
        # 1. Why standard integer division (banans // mid) is not enough:
        #    In Python, // performs FLOOR division (rounds down towards -infinity).
        #    - If banans = 15, mid = 5: 15 // 5 = 3 hours (exact division).
        #    - If banans = 7,  mid = 5:  7 // 5 = 1 hour, but Koko eats
        #      5 bananas in hour 1 and the remaining 2 bananas in hour 2.
        #      So she actually needs 2 hours (ceil).
        #
        # 2. How adding (mid - 1) forces rounding UP (Ceiling Division):
        #    Formula: ceil(A / B) == (A + B - 1) // B
        #
        #    - Case A: banans IS an exact multiple of mid (e.g., 15 and 5)
        #      (15 + 5 - 1) // 5 = 19 // 5 = 3
        #      Adding (mid - 1) is strictly less than mid, so it does not
        #      push it into the next multiple. It stays exactly 3.
        #
        #    - Case B: banans is NOT an exact multiple of mid (e.g., 7 and 5)
        #      (7 + 5 - 1) // 5 = 11 // 5 = 2
        #      Adding (mid - 1) bumps the remaining fractional part over the
        #      boundary into the next multiple of mid, giving ceil(7 / 5) = 2.
        #
        # 3. Why this is preferred in interviews / PBCs:
        #    - Precision: math.ceil(a / b) uses float division, which can lose
        #      precision with large numbers (nums[i] up to 10^9).
        #    - Performance: Integer arithmetic runs entirely on CPU integer registers
        #      with zero float-conversion or function-call overhead.
        # -------------------------------------------------------------------------
        total_hours += (banans + mid - 1) // mid 

    if total_hours <= h: 
        ans = mid 
        high = mid - 1 
    else: 
        low = mid + 1 

print(f"The minimum eating rate is : {ans} bananas/hr")
