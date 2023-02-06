## The program will find the highest overhead category

## Import required modules
from pathlib import Path
import csv

## Inspect cwd
print(Path.cwd())

def overhead_function():
    # Setting up file path for reading and writing
    fp_read = Path.cwd()/"csv_reports"/"overheads.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    fp_write.touch()

    # Assigning a blank string to the variable "category"
    category = ""
    # Assigning an empty list to the variable "overheads_list"
    overheads_list = []
    # Assigning a starting value of 0 to the variable "highest_overhead"
    highest_overhead = 0

    # Opening selected file path in mode "read" for reading and "file" is a variable assigned to the file after opening it
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        # Create csv reader object using csv
        reader = csv.reader(file)
        # Skip reading header
        next(reader)

        # Using for loop to execute the code once for each row in the reader
        for row in reader:
            # Append overheads as a list back to its empty list
            overheads_list.append(float(row[1]))

            # Using the if statement to execute the indented block of code if any overheads value is higher than that of the previous highest overhead
            if float(row[1]) > float(highest_overhead):
                highest_overhead = float(row[1])
                category = row[0]
        
        # Using .upper() to change the string to uppercase
        # Using max() to find highest value in "overheads_list" and presenting it in 2 decimal places using :,.2f
        output = f"[HIGHEST OVERHEADS] {category.upper()}: {max(overheads_list):,.2f}%"

    # Write the output to a text file
    with fp_write.open(mode="w", encoding="UTF8", newline="") as file:
        file.write(f"{output}\n") 
