import os
import csv

# path to the election data
election_csv = os.path.join('Resources', 'election_data.csv')

# create dictionaries and lists to store the data
election_data = []
data_dict = {}
output_results = {}

# calculate the number of votes received by each candidate.
def calc_percentage(election_data):
    for row in election_data:
        candidate = row[2]
        if candidate in data_dict:
            data_dict[candidate] += 1
        else:
            data_dict[candidate] = 1

# calculate the winner of the election based on popular vote.
def winner(data_dict):
    return max(data_dict, key=data_dict.get)

# create a list of strings containing the election results
def results_func(data_dict, output_results, winner):
    results = []
    total_votes = sum(data_dict.values())
    results.append("Election Results")
    results.append("-------------------------")
    results.append(f"Total Votes: {total_votes}")
    results.append("-------------------------")
    for candidate, votes in data_dict.items():
        percentage = round(votes / total_votes * 100, 3)
        output_results[candidate] = f"{percentage:.3f}% ({votes})"
        results.append(f"{candidate}: {output_results[candidate]}")
    results.append("-------------------------")
    results.append(f"Winner: {winner}")
    results.append("-------------------------")
    return results

# read the CSV file and store the data in the election_data list
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        election_data.append(row)

# calculate the election results
calc_percentage(election_data)
win = winner(data_dict)
results = results_func(data_dict, output_results, win)

# print the results
for result in results:
    print(result)

# export the results to a text file
with open("analysis/election_results.txt", "w") as file:
    # iterate through the results list and write each result to the file, separated by newlines
    for result in results:
        file.write(result + "\n")