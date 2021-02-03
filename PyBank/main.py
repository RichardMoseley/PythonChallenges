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
plChng = 0
#  find the average of those changes
avgPL = 0.00
#  greatest increase in profits(date and amount) over the entire period
gtstInc = {"date": "", "amount": 0}
#  greatest decrease in losses(date and amount) over the entire period
gtstDec = {"date": "", "amount": 0}

with open(readFile) as csvfile:
    rowIndex = 0
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for i in csvreader:
        months = months + 1
        rowIndex = rowIndex + 1
        pL = pL + int(i[1])
        date = i[0]
        gain = int(i[1])
        endPL = int(i[1])
        if (gain > gtstInc["amount"]):
            gtstInc["date"] = date
            gtstInc["amount"] = gain
        # if (gain == gtstInc["amount"]):
        #     gtstInc["date"].append = date
        if (gain < gtstDec["amount"]):
            gtstDec["date"] = date
            gtstDec["amount"] = gain
        # if (gain == gtstDec["amount"]):
        #     gtstDec["date"].append = date
        if rowIndex < 1:
            startPL = int(i[1])
    avgPL = pL / months
    plChng = endPL - startPL

# print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total Net Profit: ${pL}")
print(f"Total Change in Profit: ${plChng}")
print(f"Average Change: ${round(avgPL, 2)}")
print(f"Greatest Increase in Profits: {gtstInc['date']}(${gtstInc['amount']})")
print(f"Greatest Decrease in Profits: {gtstDec['date']}(${gtstDec['amount']})")

# write to a file
with open(writeFile, 'w') as outputFile:
    outputFile.write("Financial Analysis\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Total Months: {months}\n")
    outputFile.write(f"Total Net Profit: ${pL}\n")
    outputFile.write(f"Total Change in Profit: ${plChng}\n")
    outputFile.write(f"Average Change: ${round(avgPL, 2)}\n")
    outputFile.write(
        f"Greatest Increase in Profits: {gtstInc['date']} (${gtstInc['amount']})\n")
    outputFile.write(
        f"Greatest Decrease in Profits: {gtstDec['date']} (${gtstDec['amount']})\n")

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
