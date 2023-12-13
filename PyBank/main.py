import os
import csv

csvpath = os.path.join("/Users/Aman/BOOTCAMP/python-challenge/PyBank/Resources/budget_data.csv")
output = ("/Users/Aman/BOOTCAMP/python-challenge/PyBank/analysis/output.txt")

#Initialize variables 
total_months = 0
total_net = 0
previous_profit_loss = 0
net_change = 0
net_change_list = []
greatest_decrease = ["", 9999999999]  
greatest_increase = ["", 0]

#Open and read csv AND Read the header row first = row [0]
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

#Read through each row of data after the header
    for row in csv_reader:
        #1.The total number of months 
        total_months = total_months + 1

        #2.The net total amount of "Profit/Losses" over the entire period = row [1]
        total_net = total_net + int(row[1])

        #3a.The changes in "Profit/Losses" over the entire period (month to month)  
        if total_months > 1:
            net_change = int(row[1])- previous_profit_loss 
            net_change_list.append(net_change)  

        #4.The greatest increase in profits (date and amount) over the entire period
            if net_change > greatest_increase[1]:                              
                greatest_increase[1] = net_change
                greatest_increase[0] = row[0]                              

        #5.The greatest decrease in profits (date and amount) over the entire period
            if net_change < greatest_decrease[1]:                              
                greatest_decrease[1] = net_change
                greatest_decrease[0] = row[0]      

        #reset previous profit/loss value to current p/l to find next net_change      
        previous_profit_loss = int(row[1]) 

    #3b. Calculate the average of those changes
    average = sum(net_change_list)/len(net_change_list)


#Write in terminal 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) ")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) ")
print(f"")

with open(output, 'w') as txt_file:
    financial_header = (
        f"Financial Analysis\n"
        f"---------------------------\n")
    txt_file.write(financial_header)
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${round(average,2)}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    