import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

#define variables
total_votes = 0
candidates = []
candidate_votes = {}
votes_winner = 0

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')
    
    for row in csvreader:
    
        #Find total number of votes cast
        total_votes += 1
    
        #Create a complete list of candidates who received votes and how many votes they got
        candidate = row["Candidate"]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1
            
#Find the percentage of votes each candidate won
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    
#Find the winner of the election based on popular vote
    if votes > votes_winner:    
        votes_winner = votes
        winner = candidate    
    
#Print results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
"""

for candidate in candidate_votes:
    output += f"{candidate}: {(candidate_votes[candidate]/total_votes * 100):.3f}% ({candidate_votes[candidate]:,})\n"

output += f"""-------------------------
Winner: {winner}
-------------------------
"""
print(output)

#Export results at txt file
output_path = os.path.join("Analysis", "final_analysis.txt")

with open(output_path, 'w') as file:
    file.write(output)
   