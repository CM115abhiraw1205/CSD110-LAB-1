# Function to calculate the bill.
def calculate_bill(name, cleaning, cavity_filling, x_ray):
    # Initialize subtotal to 0 when user didn't took any service.
    subtotal = 0

    # Calculate subtotal based on services performed.
    if cleaning == 'y':
        subtotal += 60
    elif cleaning == 'n':
        subtotal += 0
    else:
        print("Invalid Input")

    if cavity_filling == 'y':
        subtotal += 200
    elif cavity_filling == 'n':
        subtotal += 0
    else:
        print("Invalid Input")

    if x_ray == 'y':
        subtotal += 100
    elif x_ray == 'n':
        subtotal += 0
    else:
        print("Invalid Input")

    # Calculate tax and total.
    tax = subtotal * 0.15
    total = subtotal + tax

    # Apply discount if applicable,
    if total > 300:
        total *= 1-0.10
    elif total > 200:
        total *= 1-0.5

    # Print receipt.
    print("")
    print("Melanie Dental Clinic")
    print("* ----------------------------*")
    print("")
    print("Receipt for patient name:", name)
    print("----------------------------------------------")
    print("Subtotal: $", subtotal)
    print("Tax: $", tax)
    if total < subtotal:
        print("Discount: $", subtotal - total)
    print("----------------------------------------------")
    print("Total: $", total)


# Take input from user.
name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
x_ray = input("Was X-Ray performed? (y/n): ")

# Calculate bill and print receipt.
calculate_bill(name, cleaning, cavity_filling, x_ray)
