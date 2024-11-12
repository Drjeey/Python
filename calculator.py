# Basic Calculator Program

# Function to perform the chosen operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation"

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display the result
    if isinstance(result, str):  # Check if result is an error message
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")
except ValueError:
    print("Invalid input! Please enter numerical values for numbers.")
