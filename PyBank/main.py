import os
import csv

readFile = "./Resources/budget_data.csv"
writeFile = "./Analysis/Analysis.txt"


#  total number of months included in the dataset
months = 0
#  net total amount of "Profit/Losses" over the entire period
pL = 0

#  changes in "Profit/Losses" over the entire period
endPL = 0
startPL = 0
frstRow_pl = 0
plChng = {"date": [], "amount": []}
valueSum = 0
#  find the average of those changes
avgPL = 0.00

with open(readFile) as csvfile:
    rowIndex = 0
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    frstRow_pl = 0
    for i in csvreader:
        if rowIndex < 1:
            frstRow_pl = int(i[1])
        months = months + 1
        rowIndex = rowIndex + 1
        pL = pL + int(i[1])
        date = i[0]
        gain = int(i[1])
        endPL = int(i[1])
        plChng['amount'].append(endPL - startPL)
        startPL = int(i[1])
        plChng["date"].append(date)
    chngMax = max(plChng["amount"][1:])
    chngMin = min(plChng["amount"][1:])
    maxIndx = plChng["amount"].index(chngMax)
    minIndx = plChng["amount"].index(chngMin)
    for values in plChng['amount']:
        valueSum += values
    trueSum = valueSum - frstRow_pl
    avgPL = valueSum / (len(plChng['amount']) - 1)

# print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total Net Profit: ${pL}")
print(f"Average Change: ${round(avgPL, 2)}")
print(
    f"Greatest Increase in Profits: {plChng['date'][maxIndx]} (${plChng['amount'][maxIndx]})")
print(
    f"Greatest Decrease in Profits: {plChng['date'][minIndx]} (${plChng['amount'][minIndx]})")

# write to a file
with open(writeFile, 'w') as outputFile:
    outputFile.write("Financial Analysis\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Total Months: {months}\n")
    outputFile.write(f"Total Net Profit: ${pL}\n")
    outputFile.write(f"Average Change: ${round(avgPL, 2)}\n")
    outputFile.write(
        f"Greatest Increase in Profits: {plChng['date'][maxIndx]} (${plChng['amount'][maxIndx]})\n")
    outputFile.write(
        f"Greatest Decrease in Profits: {plChng['date'][minIndx]} (${plChng['amount'][minIndx]})\n")

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
