import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#print("Hello world")

months = []
profit_losses = []
average_change = []


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvcol = next(csvreader)
    print(csvcol)

#Total number of months
#Net total amount of Profit/Losses
#Average change


    for row in csvreader:
        #print(row[1])
        #months=row[0]
        #print(months)
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    for x in range(1, len(profit_losses)): 
        average_change.append((int(profit_losses[x])- int(profit_losses[x-1])))

#Greatest increase
#Greatest decrease

max_index = average_change.index(max(average_change))
max_index += 1
max_date = months[max_index]

min_index = average_change.index(min(average_change))
min_index += 1
min_date = months[min_index]


#print(len(months))
#print(months)
#print(profit_losses)
#print(sum(profit_losses))
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_losses)}")
print(f"Average Change: ${sum(average_change)/len(average_change):.2f}")
print(f"Greatest Increase in Profits: {max_date} (${max(average_change)})")
print(f"Greatest Decrease in Profits: {min_date} (${min(average_change)})")

#Open a text file
with open('results.txt', 'w') as file:
    for line_number, line in enumerate(file, start=1):
        file.write("Financial Analysis")
        file.write("--------------------------------------------")
        file.write(f"Total Months: {len(months)}")
        file.write(f"Total: ${sum(profit_losses)}")
        file.write(f"Average Change: ${sum(average_change)/len(average_change):.2f}")
        file.write(f"Greatest Increase in Profits: {max_date} (${max(average_change)})")
        file.write(f"Greatest Decrease in Profits: {min_date} (${min(average_change)})")