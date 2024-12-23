def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: {original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
