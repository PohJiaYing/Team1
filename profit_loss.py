## The program will compute the difference in the net profit if net profit on the current day is lower than the previous day

## Import required modules
from pathlib import Path
import csv

## Inspect cwd
print(Path.cwd())

def profitloss_function():
    # Setting up file path for reading and writing
    fp_read = Path.cwd()/"csv_reports"/"profit_loss.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    fp_write.touch()

    # Assigning empty lists to the following variables
    day = []
    netprofit = []
    # Assigning empty lists to the following variables if there is a deficit in net profit
    deficit_day= []
    deficit_netprofit = []

    # Opening selected file path in mode "read" for reading and "file" is a variable assigned to the file after opening it
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        # Create csv reader object using csv
        reader = csv.reader(file)
        # Skip reading header
        next(reader)
        # Using for loop to execute the code once for each row in the reader
        # Using the enumerate() function in the for loop to loop "row" with a counter
        
        for count, row in enumerate(reader):
            # Append day and net profit as a list back to each empty list
            # Converting the day values to float data type using float()
            day.append(float(row[0]))
            # Converting the net profit values to integer literals using int()
            netprofit.append(int(row[4]))

            # Using the if statement to execute the indented block of code if the net profit on the current day is higher than the previous day
            if netprofit[count-1] < netprofit[count]:
                # Append day with deficit in net profit as a list back to its empty list
                deficit_day.append(row[0])
                output = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
            
            # Using the else keyword to execute the next portion of code when the if condition above is evaluated as False
            else:
                # Append amount of deficit in net profit as a list back to its empty list
                deficit_netprofit.append(netprofit[count-1] - netprofit[count])
                output =  f"[PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD {deficit_netprofit}"
    
    # Write the output to a text file
    with fp_write.open(mode="w", encoding="UTF8", newline="") as file:
            file.write(f"{output}\n") 
