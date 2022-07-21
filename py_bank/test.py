import os
import csv

#budgetdata_pybank.csv

months = []
profit_loss = []
difference = []
header = ["Month", "Profit/Loss", "Difference"]
months_new = []
profit_loss_new = []
difference_new = []
max_new = []
min_new = []

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
   
    diff = 0
    for i in range(len(profit_loss)-1):
        diff = (profit_loss[i+1])-(profit_loss[i])
        difference.append(diff)
    difference.insert(0, 0)

newlist = zip(months, profit_loss, difference)

output_path = os.path.join("budget_data.csv")

with open(output_path, "w", newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(header)
    csvwriter.writerows(newlist)

csvpath1 = os.path.join("budget_data.csv")

with open(csvpath1, newline="") as csvfile:

    csvreader1 = csv.reader(csvfile, delimiter=',')
    csvheader1 = next(csvreader1)

    for row in csvreader1:
        months_new.append(row[0])
        profit_loss_new.append(int(row[1]))
        difference_new.append(int(row[2]))

print("Financial Analysis")
print("--------------------------------------------------")
print("Total Months: " + str(len(months_new)))
print("Sum of Profit/Loss: $" + str(sum(profit_loss_new)))
print("Average Change: $" + str(round(sum(difference_new)/((len(difference_new))-1))))
print("Greatest Increase in Profits: " + str(months_new[difference_new.index(max(difference_new))]) + " ($" + str(difference_new[difference_new.index(max(difference_new))]) + ")")
print("Greatest Increase in Profits: " + str(months_new[difference_new.index(min(difference_new))]) + " ($" + str(difference_new[difference_new.index(min(difference_new))]) + ")")
