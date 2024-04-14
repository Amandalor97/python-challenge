import os
import csv

election_data = os.path.join("Resources","election_data.csv")

#print("Hello world")

votes = []
candidates = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvcol = next(csvreader)
    print(csvcol)

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

        # Create a set to get unique candidates
        unique_candidates = set(candidates)

        # Print the unique candidates
    
    for candidate in unique_candidates:
        print(candidate)

print("Election Results")
print("-------------------------------------------")
print(f"Total Votes: {len(votes)}")
print("-------------------------------------------")






