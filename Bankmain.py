
# Import modules
import os
import csv

# Set path to read data file
input_path = os.path.join (".git", "PyBank", "Resources", "budget_data.csv")

# Open input file:
with open (input_path) as csvfile:

    # Initialize the reader
    csvreader = csv.reader (csvfile, delimiter = ",")

    # Read the header row first
    csvheader = next (csvreader)

    # Set initial values

    # Define variables and set initial values 
    TotMonths = 0
    Profit = 0
    TotProfit = 0
    AvgProfit = 0
    ChgProfit = 0
    FirstProfit = 0
    SumChgProfit = 0
    MaxIncr = 0
    MaxMonth = ()
    MaxDecr = 0
    MinMonth = ()
    rowcount = 0
    

    # Count the total number of months
    for row in csvreader:
        # Determine intial profit value to deduct from SumChgProfit
        rowcount = rowcount + 1
        if rowcount == 1:
            FirstProfit = int(row[1])
        
        # Calucualte Total Months and Total Profits
        TotMonths = TotMonths + 1
        TotProfit = TotProfit + int(row[1])

         # Calculate change in Profit and Max / Min of Change
        ChgProfit = int(row[1]) - Profit
        if ChgProfit > MaxIncr:
            MaxIncr = ChgProfit
            MaxMonth = row[0]
        elif ChgProfit < MaxDecr:
            MaxDecr = ChgProfit
            MinMonth = row[0]

        # Calcualte Sum of Daliy Profit Changes
        SumChgProfit = SumChgProfit + (int(row[1]) - Profit)
                
        # Reset Profit to current period value
        Profit = int(row[1])

    # Calculate Average Daily Profit Change
    AvgProfit = round((SumChgProfit - FirstProfit) / (TotMonths -1), 2)

# Set path to write data file
output_path = os.path.join (".git", "PyBank", "Resources", "reuslt.csv")

# open output file and write ouput
with open (output_path, "w") as outputcsv:

    # Initialize csv.writer
    csvwriter = csv.writer(outputcsv, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months:", TotMonths])
    csvwriter.writerow(["Total Profits:", TotProfit])
    csvwriter.writerow(["Average Daily Change:", AvgProfit])
    csvwriter.writerow(["Greatest Incease in Profits:", MaxMonth, MaxIncr])
    csvwriter.writerow(["Greatest Decrease in Profits:", MinMonth, MaxDecr])

# Print ouptut
print ("   ")    
print ("------------------")
print ("Financial Analysis")
print ("------------------")
print (f"Total Months:  {TotMonths}")
print (f"Total Profit:  ${TotProfit}")
print (f"Average Dailiy Change: {AvgProfit}")
print (f"Greatest Increase in Profits:  {MaxMonth} (${MaxIncr})")
print (f"Greatest Decrease in Profits:  {MinMonth} (${MaxDecr})")