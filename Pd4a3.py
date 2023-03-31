# Define the value of each coin in cents
penny_value = 1
nickel_value = 5
dime_value = 10
quarter_value = 25

# Define the number of pennies in a dollar
pennies_in_dollar = 100

# Get the number of each coin from the user
num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))

# Calculate the total value of the coins in cents
totalCent = (num_pennies * penny_value) + (num_nickels * nickel_value) + \
    (num_dimes * dime_value) + (num_quarters * quarter_value)

# Convert the total value to dollars
totalDollars = totalCent / pennies_in_dollar

# Check if the total value is equal to, less than, or greater than one dollar
if totalDollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif totalDollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")
