import os
import csv

ballot_ID = []
county = []
candidate = []
new_candidate = []

csvpath = os.path.join('..','resources','election_data.csv')

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        candidate.append(row[2])

unique_candidate = set(candidate) 
new_candidate = list(unique_candidate)

count0 = 0
count1 = 0
count2 = 0
count3 = 0

for i in range(len(candidate)):
    if (candidate[i] == new_candidate[0]):
        count0 = count0 + 1
    elif (candidate[i] == new_candidate[1]):
        count1 = count1 + 1
    elif (candidate[i] == new_candidate[2]):
        count2 = count2 + 1
    elif (candidate[i] == new_candidate[3]):
        count3 = count3 + 1
percent0 = float((count0/len(candidate)*100))
percent1 = float((count1/len(candidate)*100))
percent2 = float((count2/len(candidate)*100))
percent3 = float((count3/len(candidate)*100))

#IndexError: list index out of range
finalresults0 = [new_candidate[0], new_candidate[1], new_candidate[2], new_candidate[3]]
finalresults1 = [percent0, percent1, percent2, percent3]
finalresults2 = [count0, count1, count2, count3]

print("Election Results")
print("------------------------------------")
print("Total Votes: " + str(len(candidate)))
print("------------------------------------")

print(str(new_candidate[0]) + " " + str(round(percent0,3)) +"% (" + str(count0) + ")") 
print(str(new_candidate[1]) + " " + str(round(percent1,3)) +"% (" + str(count1) + ")")
print(str(new_candidate[2]) + " " + str(round(percent2,3)) +"% (" + str(count2) + ")")
print(str(new_candidate[3]) + " " + str(round(percent3,3)) +"% (" + str(count3) + ")") 
print("------------------------------------")
print("Winner is " + str(finalresults0[finalresults2.index(max(finalresults2))]))
print("------------------------------------")
print("")