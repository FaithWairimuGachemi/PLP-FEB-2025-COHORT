def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    Applies discount only if discount_percent is 20% or higher.
    
    Args:
        price (float): Original price
        discount_percent (float): Discount percentage (0-100)
        
    Returns:
        float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent/100)
    return price

# Get user input
try:
    original_price = float(input("Enter the original price: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display result
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${final_price:.2f}")
except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
