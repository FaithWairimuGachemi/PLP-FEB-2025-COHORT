def simple_calculator():
    try:
        # User input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        # Perform the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Error: Invalid operation."

        return f"The result of {operation}ing {num1} and {num2} is: {result}"

    except ValueError:
        return "Error: Please enter valid numbers."

# Call the calculator function
print(simple_calculator())
