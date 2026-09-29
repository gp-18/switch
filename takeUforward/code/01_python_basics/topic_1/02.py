# Create variables for a product name, price, and quantity; print a readable bill line.

# Example 1:
# Input: product_name = "Laptop", price = 999.99, quantity = 2
# Output:
# Product: Laptop
# Price: $999.99
# Quantity: 2
# Total Cost: $1999.98

# Example 2:
# Input: product_name = "Book", price = 15.50, quantity = 3
# Output:
# Product: Book
# Price: $15.50
# Quantity: 3
# Total Cost: $46.50

product_name = "Laptop"
price = 999.99
quantity = 2

total_cost = price * quantity 
print(f"Product: {product_name}\nPrice: ${price}\nQuantity: {quantity}\nTotal Cost: ${total_cost}")
