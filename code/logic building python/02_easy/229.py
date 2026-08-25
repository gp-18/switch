# Form a secret society name from first letters of names in alphabetical order.
# Example 1: Input: ['Adam', 'Sarah', 'Malcolm'] -> Output: AMS
# Example 2: Input: ['Phoebe', 'Chandler', 'Rachel', 'Ross', 'Monica', 'Joey'] -> Output: CJMPRR

names = ["Adam", "Sarah", "Malcolm"]

secret_name = "".join(sorted(name[0].upper() for name in names if name))
print("Names:", names)
print("Secret society name:", secret_name)
