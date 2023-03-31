# Function to take input from the user
def takeInput():
    # Taking input for the first number
    num1 = float(input("Enter first number: "))
    # Taking input for the second number
    num2 = float(input("Enter second number: "))
    # Taking input for the operator
    operator = input("Enter operator (+,-,*,/): ")
    # Returning the input values
    return num1, num2, operator

# Function to display the result of the operation


def displayResult():
    # Calling the takeInput function to get the input values
    num1, num2, operator = takeInput()
    # Performing the operation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        # If the operator is invalid, print an error message and return
        print("Invalid operator")
        return
    # Printing the result of the operation
    print(f"{num1} {operator} {num2} = {result}")


# Calling the displayResult function
displayResult()
