import os
import csv

# Define variables
total_votes = 0
candidate_votes = {}
candidate_name =[]
candidate_name1 =[]
candidate_name2 =[]
winner = ""
winner_votes = 0

os.chdir(os.path.dirname(__file__))

# Point to Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of votes
       total_votes += 1

       #find candidate name
       candidate_name = row[2]
       if candidate_name not in candidate_votes:
         candidate_votes[candidate_name] = 0

    #Vote counts for each candidate
    candidate_votes[candidate_name] += 1
   

    #winner data
    winner = ""
    winner_votes = 0
    for candidate_name, votes in candidate_votes.items():
        percentage = round(votes/total_votes*100, 3)
    print(f"{candidate_name}: {percentage}% ({votes})")
    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes



    #print data
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
   
    #Write a text file with the results
election_file = os.path.join("analysis", "results.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes:  {total_votes}\n")
    outfile.write(f"Winner  ${winner}\n")
  
