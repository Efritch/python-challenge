# This is the solution to run for the PyBank assignment

import os
import csv

# Set path for file
csv_budget = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
day = []
budget_amount = []

# Open the CSV
with open(csv_budget) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    # Reads & prints header row in CSV file
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    
    total_profit_loss = 0

    # Loop through finding total profit/loss
    for row in csv_reader:
        
        day.append(row[0])

        budget_amount.append(row[1])

    # print(budget_amount)

total_num_months = count(day)

print(total_num_months)

for x in budget_amount:
        total_profit_loss = total_profit_loss + int(x)
    # return total_profit_loss


print(total_profit_loss)

