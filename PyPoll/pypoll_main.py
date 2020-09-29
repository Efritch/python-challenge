# This is the solution to run for the PyPoll assignment

import os
import csv
import operator

# Lists to store data
voters = []
county = []
candidate = []
khan_vote_count = []
li_vote_count = []
correy_vote_count = []
otooley_vote_count = []

# Set path for file
csv_poll_data = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV
with open(csv_poll_data) as voting_data:
    csv_reader = csv.reader(voting_data, delimiter=",")

    # Reads & prints header row in CSV file
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Create lists for data in file
    for row in csv_reader:
        
        voters.append(row[0])

        county.append(row[1])

        candidate.append(row[2])

# Find the total number of votes.
total_votes = len(voters)


# Create a list of unique counties.
county_list = set(county)


# Create a list of unique candidates.
candidate_list = set(candidate)


# Create a dictionary for all lists
candidate_data = dict(zip(voters,candidate))


# Count the total number of votes for each candidate
for x in candidate_data:
    if(candidate_data[x] == "Khan"):
        khan_vote_count.append(candidate_data[x])
    elif(candidate_data[x] == "Correy"):
        correy_vote_count.append(candidate_data[x])
    elif(candidate_data[x] == "Li"):
        li_vote_count.append(candidate_data[x])
    else:
        otooley_vote_count.append(candidate_data[x])
  

votes_for_khan = len(khan_vote_count)
votes_for_correy = len(correy_vote_count)
votes_for_li = len(li_vote_count)
votes_for_otooley = len(otooley_vote_count)

khan_vote_pct = "{:.3%}".format(votes_for_khan / total_votes)
correy_vote_pct = "{:.3%}".format(votes_for_correy / total_votes)
li_vote_pct = "{:.3%}".format(votes_for_li / total_votes)
otooley_vote_pct = "{:.3%}".format(votes_for_otooley / total_votes)


# Create a dictionary that lists the candidate and their total vote counts.
vote_summary = {"Khan": [votes_for_khan], "Correy": [votes_for_correy], "Li": [votes_for_li], "O'Tooley": [votes_for_otooley]}

winner = max(vote_summary,key = vote_summary.get)


# Prints the output in the terminal
print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_vote_pct}: ({votes_for_khan})")
print(f"Correy: {correy_vote_pct}: ({votes_for_correy})")
print(f"Li: {li_vote_pct}: ({votes_for_li})")
print(f"O'Tooley: {otooley_vote_pct}: ({votes_for_otooley})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


#File path to write to
#output_path = os.path.join("..", "Analysis", "pybank_results.csv")

#Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, "w") as csvfile:

#    csvwriter = csv.writer(csvfile, delimiter=',')

#    csvwriter.writerow(["Financial Analysis"])
#    csvwriter.writerow(["Total Months", "Total", "Average Change", "Greatest Increase Month", "Greatest Increase in Profits", "Greatest Decrease Month", "Greatest Decrease in Profits"])
#    csvwriter.writerow([total_num_months, total_profit_loss, rounded_average, max_month, max_profit_loss_change, min_month, min_profit_loss_change])