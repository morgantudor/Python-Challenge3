import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#define variables
total_months = 0
total_profit_losses = 0
profit_change = None
changes = []
dates = []

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',') 

    for row in csvreader:

        #The total number of months included in the dataset
        total_months += 1
        
        #The net total amount of "Profit/Losses" over the entire period
        total_profit_losses += int(row['Profit/Losses'])

        #The changes in "Profit/Losses" over the entire period
        if profit_change is not None:
            difference = int(row['Profit/Losses']) - profit_change
            changes.append(difference)
            dates.append(row['Date'])
        profit_change = int(row['Profit/Losses'])

#Average of the changes
average_change = sum(changes) / len(changes)
round_average = round(average_change, 2)

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_decrease = min(changes)

#The greatest decrease in profits (date and amount) over the entire period
date_max = dates[changes.index(greatest_increase)]
date_min = dates[changes.index(greatest_decrease)]

#Print data out
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses:,}")
print(f"Average Change: ${round_average:,}")
print(f"Greatest Increase in Profits: {date_max} (${greatest_increase:,})")
print(f"Greatest Decrease in Profits: {date_min} (${greatest_decrease:,})")

#Set export path
output_path = os.path.join("Analysis", "final_analysis.txt")

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${round_average}\n")
    file.write(f"Greatest Increase in Profits: {date_max} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {date_min} (${greatest_decrease})\n")