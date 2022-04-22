# Start with no money
months_needed = 0
money_on_account = 0

# While not enough money repeat
while money_on_account <= 15000:

    # Get interest on the balance
    money_on_account *= 1.01

    # Take money to the bank
    money_on_account += 1000

    # Month counter
    months_needed += 1

# Print result
print(months_needed)
