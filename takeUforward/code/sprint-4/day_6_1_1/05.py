# Q5. E-Commerce Product Inventory Controller (Practice - Encapsulation)
#
# Task:
# Design a `Product` class to manage warehouse inventory.
# Stock quantity must never become negative, and sales must be rejected if demand exceeds availability.
#
# Attributes:
# - product_id (str) : Product SKU (public).
# - product_name (str) : Display title (public).
# - price (float) : Unit selling price (public).
# - __stock_quantity (int) : Available units in warehouse (private).
#
# Methods:
# - __init__(self, product_id: str, product_name: str, price: float, initial_stock: int):
#     Initializes attributes. If initial_stock < 0, sets __stock_quantity = 0.
# - restock(self, count: int):
#     Adds count to __stock_quantity if count > 0.
#     Otherwise prints "Restock count must be positive.".
# - purchase(self, count: int) -> float:
#     If count <= 0, prints "Invalid purchase quantity." and returns 0.0.
#     If count > self.__stock_quantity, prints "Insufficient stock. Available: {self.__stock_quantity}" and returns 0.0.
#     Otherwise, deducts count from __stock_quantity and returns total cost count * price.
# - get_stock(self) -> int:
#     Returns current available stock count.
#
# Example 1:
# Input:
# laptop = Product("P-501", "Gaming Laptop", 1200.0, 10)
# print("Total Paid:", laptop.purchase(3))
# print("Remaining Stock:", laptop.get_stock())
# print("Total Paid:", laptop.purchase(10))  # Exceeds remaining stock (7)
# laptop.restock(5)
# print("Stock after restock:", laptop.get_stock())
# Output:
# Total Paid: 3600.0
# Remaining Stock: 7
# Insufficient stock. Available: 7
# Total Paid: 0.0
# Stock after restock: 12
#
# Example 2:
# Input:
# phone = Product("P-502", "Smart Phone", 800.0, 2)
# print("Total Paid:", phone.purchase(2))
# print("Remaining Stock:", phone.get_stock())
# Output:
# Total Paid: 1600.0
# Remaining Stock: 0
#
# Example 3 (Edge Case):
# Input:
# desk = Product("P-503", "Standing Desk", 300.0, -5)  # Negative stock initialized to 0
# desk.restock(-2)                                     # Negative restock rejected
# print("Purchasing from 0 stock:", desk.purchase(1))
# Output:
# Restock count must be positive.
# Insufficient stock. Available: 0
# Purchasing from 0 stock: 0.0
#
# Think About:
# - Making `__stock_quantity` private guarantees that inventory cannot drop below zero.
# - Financial calculations (count * price) only proceed after confirming stock sufficiency.
# - Time Complexity: O(1) per transaction.
# - Space Complexity: O(1) auxiliary space.

# Write your Product class below:

class Product:
    def __init__(self, product_id: str, product_name: str, price: float, initial_stock: int):
        # Write your code here
        pass

    def restock(self, count: int):
        # Write your code here
        pass

    def purchase(self, count: int) -> float:
        # Write your code here
        pass

    def get_stock(self) -> int:
        # Write your code here
        pass
