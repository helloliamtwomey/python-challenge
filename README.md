# Python Challenge: Data Analysis

## Background

This project is designed to analyze financial and poll data using Python programming language. The project includes two tasks:

PyBank - The project uses Python to read the CSV file, extract the data, and perform calculations to determine the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, the changes in "Profit/Losses" over the entire period and the average of those changes, the greatest increase in profits (date and amount) over the entire period, and the greatest decrease in profits (date and amount) over the entire period. The results are then displayed in the console and written to a text file.

PyPoll - The project uses Python to read the CSV file, extract the data, and perform calculations to determine the total number of votes cast, a complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won and the winner of the election based on popular vote. The results are then displayed in the console and written to a text file.

#### PyBank Python Script 

```

import os
import csv

# path to the budget data
Budget_csv = os.path.join('Resources', 'budget_data.csv')

# create dictionaries and lists to store the data
budget_dict = {}
delta_pnl = {}
results = []

# calculate the total P&L
def sum_pnl_func(budget_dict):
    sumpnl = 0
    # iterate through the budget dictionary and sum the P&L values
    for key, value in budget_dict.items():
        sumpnl += float(value)
    return sumpnl

# calculate the average change in P&L
def delta_pnl_func(budget_dict, totMonths):
    start = 1
    total = 0
    delta = 0
    # iterate through the budget dictionary and calculate the change in P&L
    for key, value in budget_dict.items():
        PNL = float(value)
        if start == 1:
            # add the initial value to the delta_pnl dictionary with a value of 0 
            delta_pnl[key] = delta
            start = 0            
        else:
            # calculate the change in P&L by subtracting the last month's P&L
            delta = (PNL - Last_PNL)
            delta_pnl[key] = delta
        Last_PNL = PNL
    # add up the changes in P&L
    for key, value in delta_pnl.items():
        total = total + int(value)
    # calculate the average change in P&L
    average = round(total/(totMonths-1),2)
    return average

# find the month with the greatest increase in profits
def max_profit(delta_pnl):
    maxprofit = 0
    # iterate through the delta_pnl dictionary and find the month with the greatest increase
    for key, value in delta_pnl.items():
        if int(value) > maxprofit:
            maxprofit = int(value)
            maxmonth = key
    return maxmonth, maxprofit

# find the month with the greatest decrease in profits
def min_profit(delta_pnl):
    minprofit = 0
    # iterate through the delta_pnl dictionary and find the month with the greatest decrease
    for key, value in delta_pnl.items():
        if int(value) < minprofit:
            minprofit = int(float(value))
            minmonth = key
    return minmonth, minprofit

# print the results
def output(totMonths, sumpnl, average, max, min):
    results.append("Financial Analysis")
    results.append("----------------------------")
    results.append(f"Total Months: {str(totMonths)}")
    results.append(f"Total: ${str(sumpnl)}")
    results.append(f"Average Change: ${str(average)}")
    results.append(f"Greatest Increase in Profits: {str(max[0])} (${str(max[1])})")
    results.append(f"Greatest Decrease in Profits: {str(min[0])} (${str(min[1])})")

# open the budget_data.csv file and read its contents
with open(Budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        budget_dict[row[0]] = row[1]
        totMonths = len(budget_dict)

# loading the sum of profit/losses, average change, maximum and minimum profits
sumpnl = sum_pnl_func(budget_dict)
average = delta_pnl_func(budget_dict, totMonths)
max = max_profit(delta_pnl)
min = min_profit(delta_pnl)
output(totMonths, sumpnl, average, max, min)

for result in results:
    print(result)

# export the results to a text file
with open("analysis/bank_results.txt", "w") as file:
    # iterate through the results list and write each result to the file, separated by newlines
    for result in results:
        file.write(result + "\n")
       
```

#### PyBank Results

```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198.0
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

#### PyPoll Python Script 

```

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
        
```
#### PyPoll Results

```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```
