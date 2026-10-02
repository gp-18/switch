# Write a simple decorator and use functools.wraps() to preserve the wrapped function's metadata.

# Example 1:
# Input: @my_decorator; def greet(): """Says hi"""; greet.__name__
# Output: 'greet' (preserved thanks to @wraps)

# Example 2:
# Input: greet.__doc__
# Output: 'Says hi'

