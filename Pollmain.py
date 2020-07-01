
# Import modules
import os
import csv

# Set path to read data file
input_path = os.path.join(".git", "PyPoll", "Resources", "election_data.csv" )

# Open input file:
with open (input_path) as csvfile:

    # Initialize the reader:
    csvreader = csv.reader (csvfile, delimiter = ",")

    # Read the header row first
    csvheader = next (csvreader)

    # Define variables and set inital values
    Totcount = 0
    Khancount = 0
    Khanpcg = ()
    Corcount = 0
    Corpcg = ()
    Licount = 0
    Lipcg = ()
    Toolcount = 0
    Toolpcg = ()
    Winval = ()
    Winner = ()

    for row in csvreader:

        # Calculate total votes cast and votes for each candidate
        Totcount = Totcount +1

        if row[2] == "Khan":
            Khancount = Khancount + 1
        elif row[2] == "Correy":
            Corcount = Corcount + 1
        elif row[2] == "Li":
            Licount = Licount + 1
        elif row [2] == "O'Tooley":
            Toolcount = Toolcount + 1

Khanpcg = round ((Khancount / Totcount) *100, 3)
Corpcg = round ((Corcount / Totcount) *100, 3)
Lipcg = round ((Licount / Totcount) * 100, 3)
Toolpcg = round ((Toolcount / Totcount) * 100, 3)

Winval = max(Khanpcg, Corpcg, Lipcg, Toolpcg)

if Khanpcg == Winval:
    Winner =  "Khan"
elif Corpcg == Winval:
    Winner = "Correy"
elif Lipcg == Winval:
    Winner = "Li"
elif Toolpcg == Winval:
    Winner == "O'Tooley"

# Set path to write data file
output_path = os.path.join (".git", "PyPoll", "Resources", "result.csv")

# Open output file and write outpu
with open (output_path, "w") as outputcsv:

    # Initialize csv.writer
    csvwriter = csv.writer(outputcsv, delimiter=',')

    # Write the data
    csvwriter.writerow(["Total Votes", Totcount])
    csvwriter.writerow(["Khan", Khanpcg, Khancount])
    csvwriter.writerow(["Correy", Corpcg, Corcount])
    csvwriter.writerow(["Li", Lipcg, Licount])
    csvwriter.writerow(["O'Tooley", Toolpcg, Toolcount])

# Print output in editor
print ("  ")
print ("-----------------------------")
print ("Final Results")
print ("-----------------------------")
print (f"Total Votes: {Totcount}")
print (f"Khan:  {Khanpcg}% ({Khancount})")
print (f"Correy:  {Corpcg}% ({Corcount})")
print (f"Li:  {Lipcg}% ({Licount})")
print (f"O'Tooley:  {Toolpcg}% ({Toolcount})")
print ("-----------------------------")
print (f"Winner:  {Winner}")
