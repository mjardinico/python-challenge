# Title : Module 3 Challenge
# Submitted by: Michael Jardinico
# Date: 9/24/23

# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: 
# "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and 
# calculates each of the following values:
#  * The total number of votes cast
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
#  * The winner of the election based on popular vote

#Import os, csv, sys modules
import os
import csv
import sys

#Create a csv path for the database file
csvpath = os.path.join("Resources", "election_data.csv")

# print(os.path.exists(csvpath))

#Initialize a variable to convert the election_data.csv into a list
data = []

#Loop to all rows to read the contents
with open(csvpath, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read Header
    csvheader = next(csvreader)

    total_votes = 0
    #Iterate on all rows
    for row in csvreader:
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        total_votes += 1
        data.append((ballot_id,county,candidate))


    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")

  
    #Create a dictionary to hold candidate name and their count
    candidate_counts = {}

    for i in range(1, len(data)):
        ballot_id, county, candidate = data[i]
        if candidate in candidate_counts:
            candidate_counts[candidate] += 1
        else:
            candidate_counts[candidate] = 1
    # print(candidate_counts)

    #Compute for percentage using formula (candidate votes / total votes)*100 and round to 3 decimal place
    stockham_percent = round((candidate_counts["Charles Casper Stockham"] / total_votes) * 100, 3)
    degette_percent = round((candidate_counts["Diana DeGette"] / total_votes) * 100, 3)
    doane_percent = round((candidate_counts["Raymon Anthony Doane"] / total_votes) * 100, 3)

    print(f"Charles Casper Stockham: {stockham_percent}% ({candidate_counts['Charles Casper Stockham']})")
    print(f"Diana DeGette: {degette_percent}% ({candidate_counts['Diana DeGette']})")
    print(f"Raymon Anthony Doane: {doane_percent}% ({candidate_counts['Raymon Anthony Doane']})")

    #Compute for the winner base on popular vote
    winner = None
    highest_count = 0
    for candidate, count  in candidate_counts.items():
       
        if count > highest_count:
            winner = candidate
            highest_count = count
 
    print("---------------------------")
    print(f"Winner:  {winner}")
    print("---------------------------")

#Writing the output to a text file
csv_output = os.path.join("analysis", "election_results.txt")

with open(csv_output, mode='w') as file:
    #redirect output to a text file
    print("Election Results", file=file)
    print("---------------------------", file=file)
    print(f"Total Votes: {total_votes}", file=file)
    print("---------------------------", file=file)
    print(f"Charles Casper Stockham: {stockham_percent}% ({candidate_counts['Charles Casper Stockham']})", file=file)
    print(f"Diana DeGette: {degette_percent}% ({candidate_counts['Diana DeGette']})", file=file)
    print(f"Raymon Anthony Doane: {doane_percent}% ({candidate_counts['Raymon Anthony Doane']})", file=file)
    print("---------------------------", file=file)
    print(f"Winner:  {winner}", file=file)
    print("---------------------------", file=file)


