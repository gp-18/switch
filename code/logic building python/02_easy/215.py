# Reverse a boolean value; return 'boolean expected' for non-boolean input.
# Example 1: Input: True -> Output: False
# Example 2: Input: 'hello' -> Output: boolean expected

def reverse_bool(val):
    if isinstance(val, bool):
        return not val
    return "boolean expected"

print("True ->", reverse_bool(True))
print("False ->", reverse_bool(False))
print("1 ->", reverse_bool(1))
