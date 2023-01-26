import os
import csv

months = []
profit_loss = []
difference = []
header = ["Month", "Profit/Loss", "Difference"]
months_new = []
profit_loss_new = []
difference_new = []

# Open and read csv file 'budget_data.csv'
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Skip the header row
    next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
   
    diff = 0
    for i, value in enumerate(profit_loss):
        if i > 0:
            diff = value - profit_loss[i-1]
            difference.append(diff)
    difference.insert(0, profit_loss[0])

newlist = zip(months, profit_loss, difference)

output_path = os.path.join("budget_data.csv")

with open(output_path, "w", newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

# Write data to output file
csvwriter.writerows(newlist)

# Close output file
csvfile.close()

csvpath1 = os.path.join("budget_data.csv")

with open(csvpath1, newline="") as csvfile:

    csvreader1 = csv.reader(csvfile, delimiter=',')
    csvheader1 = next(csvreader1)

    for row in csvreader1:
        months_new.append(row[0])
        profit_loss_new.append(int(row[1]))
        difference_new.append(int(row[2]))

# Find maximum and minimum values in difference_new list
max_value = max(difference_new)
min_value = min(difference_new)
max_index = difference_new.index(max_value)
min_index = difference_new.index(min_value)

# Get corresponding month and profit/loss values
max_month = months_new[max_index]
max_profit = profit_loss_new[max_index]
min_month = months_new[min_index]
min_profit = profit_loss_new[min_index]

# Print analysis to terminal
print("Financial Analysis")
print("--------------------------------------------------")
print("Total Months: " + str(len(months_new)))
print("Total: $" + "{:,}".format(sum(profit_loss_new)))
print("Average Change: $" + "{:,.2f}".format(round((sum(difference_new)/((len(difference_new))-1)), 2)))
print("Greatest Increase in Profits: " + max_month + " ($" + "{:,}".format(max_value) + ")")
print("Greatest Decrease in Profits: " + min_month + " ($" + "{:,}".format(min_value) + ")")
