import csv
import os

print(os.getcwd())
# print(__file__)
# print(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track votes per candidate
candidates = []  # List of candidates
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Add to the total vote count
        total_votes += 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate is not already in the list, add them and initialize their vote count
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
            candidates.append(candidate_name)

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Output the election results
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")

    txt_file.write(election_results)

    # Calculate the percentage of votes for each candidate and the winner
    for candidate in candidate_votes:
        # Retrieve the vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Print each candidate's vote count and percentage (to terminal)
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

        # Determine winning candidate and vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)