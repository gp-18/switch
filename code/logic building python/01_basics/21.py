# Print the multiplication table of a given number (n × 1 to n × 10).

number = int(input("Enter the number : "))


for i in range(1,11) :
  print(f"{number} x {i} = {number * i}")