# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote.

# Adding dependencies
import csv
import os

# Assign a variable for the file to load a file from path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Total votes counter
total_votes = 0
# Candidate options and candidate votes
candidate_option = []
# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:

        total_votes += 1

        # Get candidate name for each row
        candidate_name = row[2]
        # If candidate not in the list, add it
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate"s count.
        candidate_votes[candidate_name] += 1

# print(candidate_option)
# print(candidate_votes)

for candidate_name in candidate_option:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100
    print(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Votes Count: {winning_count:,}\n"
    f"winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)


# with open(file_to_save,"w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson\n ")
