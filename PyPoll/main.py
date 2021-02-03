import os
import csv

readFile = "./Resources/election_data.csv"
writeFile = "./Analysis/Analysis.txt"

# The total number of votes cast
totalCast = 0

# A complete list of candidates who received votes
canList = []

# The percentage of votes each candidate won
# REMOVED VARIABLE AND ADDED TO DICT

# The total number of votes each candidate won
allCan_data = []
canVote = {"Candidate": [], "Votes": [], "VotePerc": []}

# The winner of the election based on popular vote.
winner = ""

with open(readFile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for i in csvreader:
        totalCast = totalCast + 1
        if i[2] not in canList:
            canList.append(i[2])
        if i[2] not in canVote["Candidate"]:
            canVote["Candidate"].append(i[2])
        allCan_data.append(i[2])
    for j in canVote["Candidate"]:
        canVote["Votes"].append(allCan_data.count(j))
    for k in canVote["Votes"]:
        percent = (k / totalCast)*100
        canVote["VotePerc"].append(round(percent, 3))

    topVote = max(canVote["Votes"])
    voteIndex = canVote["Votes"].index(topVote)
    winner = canVote["Candidate"][voteIndex]


# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000 % (2218231)
# Correy: 20.000 % (704200)
# Li: 14.000 % (492940)
# O'Tooley: 3.000 % (105630)
# -------------------------
# Winner: Khan
# -------------------------
