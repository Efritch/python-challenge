# This is the solution to run for the PyBank assignment

import os
import csv
import statistics

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


# Finds the total number of months in the data file
total_num_months = len(day)

#print(total_num_months)

for x in budget_amount:
        total_profit_loss = total_profit_loss + int(x)
    # return total_profit_loss

#print(total_profit_loss)


# Find monthly profit/loss changes
for i in range(1, len(budget_amount)):
    monthly_difference.append(int(budget_amount[i]) - int(budget_amount[i - 1]))

# print("monthly difference: ", str(monthly_difference))


# Find the average monthly change in profit/loss values
avg_profit_loss_change = statistics.mean(monthly_difference)
#print(avg_profit_loss_change)
rounded_average = round(avg_profit_loss_change,2)
#print(rounded_average)

# Find the largest monthly change in profit/loss and the month it occurred
max_profit_loss_change = max(monthly_difference)
#print(max_profit_loss_change)

max_pos = monthly_difference.index(max_profit_loss_change)
#print(max_pos)

max_month = day[max_pos + 1]
#print(max_month)


# Find the smallest monthly change in profit/loss and the month it occurred
min_profit_loss_change = min(monthly_difference)
#print(min_profit_loss_change)

min_pos = monthly_difference.index(min_profit_loss_change)
#print(min_pos)

min_month = day[min_pos + 1]
#print(min_month)

print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_num_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${(rounded_average)}")
print(f"Greatest Increase in Profits: {max_month}: ({max_profit_loss_change})")
print(f"Greatest Decrease in Profits: {min_month}: ({min_profit_loss_change})")

#File path to write to
output_path = os.path.join("..", "Analysis", "pybank_results.csv")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow(["Total Months: "] + ['total_num_months'])
    csvwriter.writerow(["Total: $"] + ['total_profit_loss'])
    csvwriter.writerow(["Average Change: $"] + ['rounded_average'])
    csvwriter.writerow(["Greatest Increase in Profits: "] + ['max_month'] + [" "] + ['max_profit_loss_change'])
    csvwriter.writerow(["Greatest Decrease in Profits: "] + ['min_month'] + [" "] + ['min_profit_loss_change'])
