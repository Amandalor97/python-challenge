import os
import csv

election_data = os.path.join("Resources","election_data.csv")

total_votes = []
candidates = []
unique_candidates = []
count_votes = []
percentage_votes = []
votes = 0

#Skipping the headrow
#Total number of votes cast

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvcol = next(csvreader)
    print(csvcol)

    for row in csvreader:
        total_votes.append(row[0])
        candidates.append(row[2])
        votes += 1
      
print("Election Results")
print("-------------------------------------------")
print(f"Total Votes: {len(total_votes)}")
print("-------------------------------------------")

#Create a set to get unique candidates
#CTV=Candidates total votes -> Counting the occurence of the names of the candidates which represents the total number of votes per candidates      
#PTV=Percentage total votes -> Finding the percentage of votes by dividing the votes per candidates by the overall number of votes and then *100
#Finding the winner by pointing out the candidates who has the max votes

for x in set(candidates):
        unique_candidates.append(x)
        CTV = candidates.count(x)
        count_votes.append(CTV)
        PTV = (CTV/votes)*100
        percentage_votes.append(PTV)

Max_count = max(count_votes)
Winner = unique_candidates[count_votes.index(Max_count)]

for i in range(len(unique_candidates)):
     print(f"{unique_candidates[i]}: {percentage_votes[i]:.3f}% ({count_votes[i]})")

print("-------------------------------------------")
print(f"Winner: {Winner}")
print("-------------------------------------------")

#Open a text file
with open('election_results.txt', 'w') as file:
     file.write("Election Results")
     file.write("-------------------------------------------")
     file.write(f"Total Votes: {len(total_votes)}")
     file.write("-------------------------------------------")
     file.write(f"{unique_candidates[i]}: {percentage_votes[i]:.3f}% ({count_votes[i]})")
     file.write("-------------------------------------------")
     file.write(f"Winner: {Winner}")
     file.write("-------------------------------------------")
