import os
import csv

csvpath = ("/Users/Aman/BOOTCAMP/python-challenge/PyPoll/Resources/election_data.csv")
output = ("/Users/Aman/BOOTCAMP/python-challenge/PyPoll/analysis/output.txt")

#Initialize variables 
total_votes = 0
candidate = []
candidate_vote = {}
candidate_names = []
winner = ""
winning_votes = 0
popular_vote = 0

#Open and read csv AND read the header row first = row [0]
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Election Results")

#Read through each row of data after the header
    for row in csv_reader:
        #1.The total number of votes cast
        total_votes = total_votes + 1

        #2.A complete list of candidates who received votes
        candidate = row[2]
        
        if candidate not in candidate_names: 
            candidate_names.append(candidate)
            candidate_vote[candidate] = 0
           #then add them 
        candidate_vote[candidate] = candidate_vote[candidate] + 1

print("-----------------------")  
print(f"Total Votes: {total_votes}")
print("-----------------------")  

        #3.The total number of votes and percentage of votes each candidate won
with open(output, 'w') as txt_file:
    election_header = (
        f"Election Results\n"
        f"--------------------------\n")
    txt_file.write(election_header)
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------\n")

    for candidate in candidate_vote: 
        winning_votes = candidate_vote[candidate]
        percentage = (winning_votes/total_votes) * 100

        #4.The winner of the election based on popular vote
        if winning_votes > popular_vote:
            popular_vote = winning_votes
            winner = candidate
        final_output = (f"{candidate}: {percentage:.3f}% ({winning_votes})\n")
        print(final_output)
        txt_file.write(final_output)

    txt_file.write("----------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("----------------------------\n")
        
#Print to terminal
    print("-----------------------")   

    print(f"Winner: {winner}")
   
    print("-----------------------") 
