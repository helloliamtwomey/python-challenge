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