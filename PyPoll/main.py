# Import ability to read across operating systems and read csv files
import os
import csv
from collections import Counter

# Create path to read csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Store the three columns as lists
voter_id = []
county = []
candidate = []

# Read the CSV file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip column headers
    next(csvreader)

    for row in csvreader:
        # Add the voter id to a list
        voter_id.append(row[0])

        # Add the county to a list
        county.append(row[1])

        # Add cadidates to a list
        candidate.append(row[2])

# Learned set function from "https://datagy.io/python-count-unique-values-list/"
# Counting unique voter ids in column 1 to find total votes
set = set(voter_id)
voter_total = len(set)

# Using the imported Counter function to count the # of votes each candidate got
win_count = Counter(list(candidate))

# Begin printed output of results
print (f'Election Results')
print (f'----------------------------------')
print (f'Total Votes: {voter_total}')
print (f'----------------------------------')

# Iterate through the unique candidate list to list the candidates, the votes they recieved, and the percentage of votes they won
for wins in win_count:
    print(f'{wins}: {round(((win_count[wins]/voter_total)*100),3)}% ({win_count[wins]})')

print (f'----------------------------------')
# Using the max function to find the winner in the win_count dictionary the print it out
#https://datagy.io/python-get-dictionary-key-with-max-value/
big_winner = max(win_count, key = win_count.get)
print (f'Winner: {big_winner}')
print (f'----------------------------------')

# writing to a txt file using a file handler - https://www.youtube.com/watch?v=walXPsausPI&ab_channel=ProgrammingKnowledge
output_file = os.path.join('analysis',"written_analysis_pypoll.txt")

with open(output_file,"w") as fh:

    fh.write (f'Election Results \n')
    fh.write (f'----------------------------------\n')
    fh.write (f'Total Votes: {voter_total}\n')
    fh.write (f'----------------------------------\n')
    for wins in win_count:
        fh.write(f'{wins}: {round(((win_count[wins]/voter_total)*100),3)}% ({win_count[wins]})\n')
    fh.write(f'----------------------------------\n')
    big_winner = max(win_count, key = win_count.get)
    fh.write(f'Winner: {big_winner}\n')
    fh.write(f'----------------------------------\n')


    fh.close()

