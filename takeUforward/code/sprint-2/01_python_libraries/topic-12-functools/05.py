# Write a simple decorator and use functools.wraps() to preserve the wrapped function's metadata.

# Example 1:
# Input: @my_decorator; def greet(): """Says hi"""; greet.__name__
# Output: 'greet' (preserved thanks to @wraps)

# Example 2:
# Input: greet.__doc__
# Output: 'Says hi'

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Says hi"""
    return "Hello!"

print(f"greet.__name__ = '{greet.__name__}'")
print(f"greet.__doc__ = '{greet.__doc__}'")
