# python-challenge

Helllo, in this repository you will find my homework for the Module 3 Challenge. This homework has been made with the help of differents sources: Tutor, Xpert Learning Assistant, Stack Overflow, Geeksforgeeks, TA & and myself Amanda Lor.




Instructions:

PyBank Instructions:
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

-The total number of months included in the dataset

-The net total amount of "Profit/Losses" over the entire period

-The changes in "Profit/Losses" over the entire period, and then the average of those changes

-The greatest increase in profits (date and amount) over the entire period

-The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis

----------------------------
Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.




PyPoll Instructions:
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

-The total number of votes cast

-A complete list of candidates who received votes

-The percentage of votes each candidate won

-The total number of votes each candidate won

-The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results

-------------------------

Total Votes: 369711

-------------------------
Charles Casper Stockham: 23.049% (85213)

Diana DeGette: 73.812% (272892)

Raymon Anthony Doane: 3.139% (11606)

-------------------------

Winner: Diana DeGette

-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.




Breakdown of the homework: 

PyBank: 

1) Found the Total Months with len

2) Found the Total with sum 

3) Found the Average Change  with sum/len

4) Found the Greatest Increase with max

5) Found the Greatest Decrease with min

6) Opened a text file


PyPoll:

1) Found Total Votes with len

2) Used unique to find each candidate 

3) Found the Candidates Total Votes by counting the occurence of each names 

4) Found the Percentage Total Votes by dividing the votes per candidates by the overall number of votes and then *100

5) Found the winner with max

6) Opened a text file
