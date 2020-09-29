# This is the solution to run for the PyPoll assignment

import os
import csv
import statistics

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
print(total_votes)

# Create a list of unique counties.
county_list = set(county)
print(county_list)

# Create a list of unique candidates.
candidate_list = set(candidate)
print(candidate_list)

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
  

print(len(khan_vote_count))
print(len(correy_vote_count))
print(len(li_vote_count))
print(len(otooley_vote_count))

