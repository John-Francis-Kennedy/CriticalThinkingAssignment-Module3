# Part 1: Meal Calculator

# Ask user for food charge
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display results
print("\nMeal Details:")
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")
