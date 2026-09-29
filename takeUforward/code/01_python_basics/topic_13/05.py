# Create a menu that repeats until the user chooses "exit"; ensure every path either updates the condition or exits.

# Example 1:
# Input: "1" (greet), then "exit"
# Output: "Hello!" -> "Exiting menu. Goodbye!"

# Example 2:
# Input: "exit"
# Output: "Exiting menu. Goodbye!"

choice = ""

while choice != "exit":
    print("\n--- Menu ---")
    print("1: Say Hello")
    print("exit: Quit")
    
    choice = input("Enter choice: ").strip().lower()
    
    if choice == "1":
        print("Hello!")
    elif choice == "exit":
        print("Exiting menu. Goodbye!")
    else:
        print("Invalid choice, please try again.")
