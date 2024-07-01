# Create a dictionary with electricity bills from January to December
electricity_bills = {
    'January': 120.50,
    'February': 110.75,
    'March': 130.40,
    'April': 125.60,
    'May': 140.30,
    'June': 135.80,
    'July': 145.00,
    'August': 150.25,
    'September': 142.70,
    'October': 138.90,
    'November': 147.55,
    'December': 152.80
}

# Calculate the total bill for the year
total_bill = sum(electricity_bills.values())

# Calculate the average monthly bill
average_bill = total_bill / len(electricity_bills)

# Print the total and average bill, formatted to 2 decimal places
print(f"Total Electricity Bill for the Year: rs-{total_bill:.2f}")
print(f"Average Monthly Electricity Bill: rs-{average_bill:.2f}")