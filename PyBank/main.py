# Import ability to read across operating systems and read csv files
import os
import csv


# Create path to read csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Print heading to output info
print("Financial Analysis")
print("---------------------------------------------------------------")

# Store the two columns as lists
date = []
change_amount = []
profit_change = []


# Read the CSV file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip column headers
    next(csvreader)
     
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add change and cast the variable as a int
        change_amount.append(float(row[1]))
        
# Learned set function from "https://datagy.io/python-count-unique-values-list/"
# Counting unique months in column 1 to find total months
set = set(date)
month_total = len(set)


# Running a loop to make a list that is the changes from month to month
for x in range(len(change_amount)-1):
    profit_change.append(change_amount[x+1]-change_amount[x])

# Find the average of the monthly changes
change_avg = round(sum(profit_change)/len(profit_change),2)

# Find the total of changes in the data over the given period of time
change_total = round(sum(change_amount))

# Find the greatest increase
grt_profit = round(max(profit_change))
# Use index to find the month associated with the month the max change happened
grt_profit_month = profit_change.index(max(profit_change)) + 1

# Find the greatest decrease
lst_profit = round(min(profit_change))
# Use index to find the month line associated with the month the min change happened
lst_profit_month = profit_change.index(min(profit_change)) + 1


# Print out all calculations
print (f'Total months: {month_total}')
print (f'')
print (f'Total: ${change_total}')
print (f'')
print (f'Average Change: {change_avg}')
print (f'')
# use the index function to print out the month that had the greatest profit/biggest loss from the date list
print (f'Greatest Increase in Profits: {date[grt_profit_month]} $({grt_profit})')
print (f'')
print (f'Greatest Decrease in Profits: {date[lst_profit_month]} $({lst_profit})')

# writing to a txt file using a file handler - https://www.youtube.com/watch?v=walXPsausPI&ab_channel=ProgrammingKnowledge



output_file = os.path.join('analysis',"written_analysis.txt")

with open(output_file,"w") as fh:

    fh.write("Financial Analysis\n")
    fh.write("---------------------------------------------------------------\n")
    fh.write(f'Total months: {month_total}\n')
    fh.write(f'\n')
    fh.write(f'Total: ${change_total}\n')
    fh.write(f'\n')
    fh.write(f'Average Change: {change_avg}\n')
    fh.write(f'\n')
    fh.write(f'Greatest Increase in Profits: {date[grt_profit_month]} $({grt_profit})\n')
    fh.write(f'\n')
    fh.write(f'Greatest Decrease in Profits: {date[lst_profit_month]} $({lst_profit})\n')


    fh.close()










 