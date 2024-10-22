import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_losses = 0
changes = []
months = []

# Variables to track the greatest increase and decrease
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Read the first row (so we can calculate changes in the next iteration)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_losses = int(first_row[1])
    
    # Loop through the remaining rows in the dataset
    for row in reader:
        # Track the total number of months
        total_months += 1
        
        # Track the net total amount of "Profit/Losses"
        total_net += int(row[1])

        # Calculate the change in "Profit/Losses" between months
        net_change = int(row[1]) - previous_profit_losses
        changes.append(net_change)
        months.append(row[0])
        
        # Set the previous row profit/loss for the next loop iteration
        previous_profit_losses = int(row[1])
        
        # Calculate the greatest increase in profits (date and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        
        # Calculate the greatest decrease in profits (date and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes)

# Output the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Output the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")