# This is the solution to run for the PyBank assignment

import os
import csv
import numpy as np

# Set path for file
csv_budget = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
day = []
budget_amount = []
monthly_difference = []

# Open the CSV
with open(csv_budget) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    # Reads & prints header row in CSV file
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
    
    total_profit_loss = 0

    # Loop through finding total profit/loss
    for row in csv_reader:
        
        day.append(row[0])

        budget_amount.append(row[1])

    # print(budget_amount)

# Finds the total number of months in the data file
total_num_months = len(day)

print(total_num_months)

for x in budget_amount:
        total_profit_loss = total_profit_loss + int(x)
    # return total_profit_loss

print(total_profit_loss)
#print(budget_amount)

# Find monthly profit/loss changes
for i in range(1, len(budget_amount)):
    monthly_difference.append(int(budget_amount[i]) - int(budget_amount[i - 1]))

print("monthly difference: ", str(monthly_difference))

# Find the largest monthly change in profit/loss
max_profit_loss_change = max(monthly_difference)
print(max_profit_loss_change)

# Find the smallest monthly change in profit/loss
min_profit_loss_change = min(monthly_difference)
print(min_profit_loss_change)

