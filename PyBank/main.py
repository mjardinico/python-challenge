# Title:  Module 3 Challenge Part I
# Submitted by:  Michael Jardinico
# Date submitted: 9/24/23
# #PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period

#Import os and csv modules
import os
import csv
import sys

#Create a csv path for the database file
csvpath = os.path.join("Resources","budget_data.csv")

#Convert the data into a list
data = []

#Using csv module to read contents
with open(csvpath, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read header 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    #Read each row in the data
    #Compute for total months and total amount
    total_months = 0
    total_amount = 0   
    for row in csvreader:
        #assign variable to date and profit/losses
        date = row[0]
        profit_losses = int(row[1])
        total_months += 1
        total_amount = total_amount + profit_losses

        # Append the data with date and profit_losses
        data.append((date, profit_losses))

    # print(data)
    
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months:  {total_months}")         
    print(f"Total:  {total_amount}")                


    #Create a for loop to compute for changes in Profit/Losses
    changes = []
    
    
    for i in range(1, len(data)):
        date, profit = data[i]     #unpack the date and profit
        _, prev_profit = data[i - 1] #previous profit
        change = profit - prev_profit
        changes.append((date, change))
    # print(changes)


    #Compute for Average Change
    total_numeric_changes = 0     #get total changes in the list changes
    total_count = 0
    for _, change in changes:
        total_numeric_changes += change
        total_count += 1
    # print(total_numeric_changes)

    average_change = round(total_numeric_changes/total_count, 2)
    print(f"Average Changes: (${average_change})")


    #Check for greatest increase in profit
    greatest_increase = changes[0][1]
    greatest_increase_date = changes[0][0]
    for date, change in changes:
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date

    #Check for greatest decrease in profit
    greatest_decrease = changes[0][1]
    greatest_decrease_date = changes[0][0]
    for date, change in changes:
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date


    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Writing the output to a text file
csv_output = os.path.join("analysis","financial_analysis.txt")

with open(csv_output, mode="w") as file:
    #Redirect output to the text file
    print("Financial Analysis", file=file)
    print("------------------------------------", file=file)
    print(f"Total Months:  {total_months}", file=file)         
    print(f"Total:  {total_amount}", file=file)    
    print(f"Average Changes: (${average_change})", file=file)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=file)





