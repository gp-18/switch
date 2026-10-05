# Generate cumulative sums and cumulative products using itertools.accumulate().

# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: Cumulative sums: [1, 3, 6, 10]

# Example 2:
# Input: nums = [1, 2, 3, 4], func = operator.mul
# Output: Cumulative products: [1, 2, 6, 24]

import itertools
import operator

nums = [1, 2, 3, 4]
cum_sums = list(itertools.accumulate(nums))
cum_prods = list(itertools.accumulate(nums, operator.mul))
print(f"Cumulative sums: {cum_sums}")
print(f"Cumulative products: {cum_prods}")
