# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
fileLoad = os.path.join("budget_data.csv")  # Input file path

# file to hold the output of the financial data
file_to_output = os.path.join("financial_data.txt")


# Define variables to track the financial data
total_months = 0                    # initializes the total months to 0
total_net = 0                       # initializes the total net to 0
monthly_changes = []                # initializes the monthly changes 
months = []                         # initialize the list of months


# Open and read the csv
with open(fileLoad) as budget_data:
    csvreader = csv.reader(budget_data)

    # Skip the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment the count of the total months
    total_months += 1
    # add on to the total net
    total_net += float(firstRow[1])
    # establish the previous profit/loss
    previousBudget = float(firstRow[1])

    # Process each row of data
    for row in csvreader:
        # increment the count of the total months
        total_months += 1

        # Track the total
        total_net += float(row[1])

        # Track the net change
        netChange = float(row[1]) - previousBudget
        # add on to the list of monthly changes
        monthly_changes.append(netChange)
        # add the first month that a change occurred
            # month is in index 0
        months.append(row[0])
        # update the previous budget
        previousBudget = float(row[1])
        # calculate the average net change per month
        average_change = sum(monthly_changes) / len(monthly_changes)
        r_average_change = round(average_change, 2)                 # rounds the average change to 2 decimal places

        greatest_increase = [months[0], monthly_changes[0]]         # holds the month and the value of the greatest increase
        greatest_decrease = [months[0], monthly_changes[0]]         # holds the month and the value of the greatest decrease

        # using loop to calculate the index of the greatest and least monthly change
        for m in range(len(monthly_changes)):
            # Calculate the greatest increase in profits (month and amount)
            if(monthly_changes[m] > greatest_increase[1]):
                # if the value is greater than the greatest increase, that value becomes the new greatest increase
                greatest_increase[1] = monthly_changes[m]
                # update the month
                greatest_increase[0] = months[m]

            # Calculate the greatest decrease in losses (month and amount)
            if(monthly_changes[m] < greatest_decrease[1]):
                # if the value is greater than the greatest increase, that value becomes the new greatest decrease
                greatest_decrease[1] = monthly_changes[m]
                # update the month
                greatest_decrease[0] = months[m]


# Calculate the average net change across the months


# Generate the output summary
output = (
    f"Financial Analysis \n"
    f"--------------------------- \n\n"
    f"Total Months: {total_months}\n\n"
    f"Total: {total_net:,.2f}\n\n"
    f"Average Change: {r_average_change}\n\n"
    f"Greatest Increase in Profits: {greatest_increase}\n\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n\n"
)
# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
