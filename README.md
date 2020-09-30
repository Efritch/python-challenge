# python-challenge
This repository contains all files for the Python homework assignment. I have completed the following homework items:

1) PyBank
2) PyPoll
3) PyBoss

Resources:
All resource files used in the written code are stored in the Resources folder. Below is a list of these files.
1) budget_data.csv
2) election_data.csv
3) employee_data.csv

Analysis Results:
All answers to the data analysis are stored .csv files located in the Analysis folder. Below is a list of the files.
1) pybank_results.csv
2) pypoll_results.csv
3) pyboss_results.csv

PyBank:
The solution for PyBank (main.py) reads data from a .csv file. This data contains monthly profit/loss information for a company. The python code sorts and manipulates the data to find the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire time period covered in the dataset
* An average of the monthly change in "Profit/Losses" over time period covered in the dataset
* The month that had the greatest increase in profits and what the profit was for that month
* The month that had the greatest decrease in profits and what the loss was for that month

All of these items are printed out in the terminal when the code is run. The code for PyBank also creates a new .csv file (pybank_results.csv) that contains all of the items determined from the data analysis.


PyPoll:
The solution for PyPoll (pypoll_main.py) reads data from a .csv file. This data contains data for a local election. The python code sorts and manipulates the data to find the following:
* The total number of votes cast during the local election
* A list of the candidates who received votes in the local election
* The total number of votes each candidate received
* The percent of the total votes each candidate received
* The winner of the election, which is the candidate that received the most votes

All of these items are printed out in the terminal when the code is run. The code for PyPoll also creates a new .csv file (pypoll_results.csv) that contains all of the items determined from the data analysis.


PyBoss:
