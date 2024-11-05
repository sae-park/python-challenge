# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("election_data.csv")  # Input file path
file_to_output = os.path.join("election_analysis.txt")  # Output file path


# Initialize variables to track the election data
total_votes = 0                              # Track the total number of votes cast
candidates = []                              # list that holds the candidate
candidateVotes = {}                          # dictionary that will hold the votes each candidate receives 
winning_count = 0                            # holds the winning count
winning_candidate = ""                       # holds the winning candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1        # same as totalVotes = totalVotes + 1


        if row[2] not in candidates:
            # if the candidate is not in the list, add the candidate to the list of candidates
            candidates.append(row[2])

            # add the value to the dictionary as well
            # { "key": value }
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1
        
        else: 
            # the candidate is in the list
            # add a vote to the candidate's count
            candidateVotes[row[2]] += 1
            

    voter_output = ""

    for candidate in candidateVotes:
        # get the vote count and the percentage of the votes
        votes = candidateVotes.get(candidate)
        votePct = (float(votes) / float(total_votes)) * 100.00

        voter_output += f"{candidate}: {votePct:.3f}% ({votes})\n\n"

        # compare the votes to the winning count
        if votes > winning_count:
            # update the votes to be the new winning count
            winning_count = votes
            # update the winning candidate
            winning_candidate = candidate
    winner_output = f"Winner: {winning_candidate}\n"
        
# create an output variable to hold the output
output = (
    f"\nElection Results\n\n"
    f"-------------------------------"
    f"\n\nTotal Votes: {total_votes:,}\n\n"
    f"-------------------------------"
    f"\n\n{voter_output}"
    f"-------------------------------"
    f"\n\n{winner_output}\n"
    f"-------------------------------"
    )
# displays the output to the terminal
print(output)

# print the results and export the data to a text file
with open(file_to_output, "w") as textFile:
    # write the output to the text file
    textFile.write(output)

 