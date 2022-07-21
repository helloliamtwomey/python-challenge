import os
import csv

voter_ID = []
county = []
candidates = []
new_candidates = []

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        candidates.append(row[2])
    
unique_candidates = set(candidates) 
new_candidates = list(unique_candidates)

count0 = 0
count1 = 0
count2 = 0
count3 = 0

for i in range(len(candidates)):
    if (candidates[i] == new_candidates[0]):
        count0 = count0 + 1
    elif (candidates[i] == new_candidates[1]):
        count1 = count1 + 1
    elif (candidates[i] == new_candidates[2]):
        count2 = count2 + 1
    elif (candidates[i] == new_candidates[3]):
        count3 = count3 + 1
percent0 = float((count0/len(candidates)*100))
percent1 = float((count1/len(candidates)*100))
percent2 = float((count2/len(candidates)*100))
percent3 = float((count3/len(candidates)*100))

finalresults0 = [new_candidates[0], new_candidates[1], new_candidates[2], new_candidates[3]]
finalresults1 = [percent0, percent1, percent2, percent3]
finalresults2 = [count0, count1, count2, count3]

print("Election Results")
print("------------------------------------")
print("Total Votes: " + str(len(candidates)))
print("------------------------------------")

print(str(new_candidates[0]) + " " + str(round(percent0,3)) +"% (" + str(count0) + ")") 
print(str(new_candidates[1]) + " " + str(round(percent1,3)) +"% (" + str(count1) + ")")
print(str(new_candidates[2]) + " " + str(round(percent2,3)) +"% (" + str(count2) + ")")
print(str(new_candidates[3]) + " " + str(round(percent3,3)) +"% (" + str(count3) + ")") 
print("------------------------------------")
print("Winner is " + str(finalresults0[finalresults2.index(max(finalresults2))]))
print("------------------------------------")
print("")



# count0 = candidates.count(new_candidates[0])
# print(str(new_candidates[0]) +": " + str(count0))
# count1 = candidates.count(new_candidates[1])
# print(str(new_candidates[1]) +": " + str(count1))
# count2 = candidates.count(new_candidates[2])
# print(str(new_candidates[2]) +": " + str(count2))
# count3 = candidates.count(new_candidates[3])
# print(str(new_candidates[3]) +": " + str(count3))