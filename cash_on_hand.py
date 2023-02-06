## The program will compute the difference in Cash-on-Hand if the current day is lower than the previous day

from pathlib import Path 
import csv 
 
# ## inspect cwd 
# print(Path.cwd()) 
 
def coh_function(): 
    """ 
    - This function will check if there is a surplus or deficit in cash on hand  
    """ 
 
fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv" 
 
##setup filepath for reading 
fp_read = Path.cwd()/"csv_reports"/"Cash on Hand.csv" 
 
fp_write = Path.cwd()/"Summary_Report.txt" 
 
# fp_write.touch() 
 
# read the csv file to append profit and quantity from the csv. 
with fp.open(mode="r", encoding="UTF-8", newline="") as file: 
    reader = csv.reader(file) 
    next(reader) # skip header 
 
## this function will calculate the difference in cash on hand  
 
# creating 2 empty lists within the open reader file  
    cluster1 = [] 
    cluster2 = [] 
 
# using for loop to store day and cash on hand amount to the 2 empty lists 
    for day, coh in reader: 
        cluster1.append(day) 
        cluster2.append(coh) 
 
# creating another 2 empty lists 
    empty_list1 = [] 
    empty_list2 = [] 
 
# converting integer to float for the 2 empty list 
    int1 = [float(num) for num in empty_list1] 
    int2 = [float(num) for num in empty_list2] 
 
# using for loop 
    for value in reader: 
 
# assigning index 0 
        lists = list[0] 
 
# assigning index 1 
        list1=list[1] 
 
# appending values to empty lists 
        empty_list1.append(list1) 
        empty_list2.append(int1) 
 
# creating file path to Summart_Report.txt 
fp = Path.cwd()/"Summary_Report.txt" 
 
# opening file path in write mode 
with fp.open(mode = "w", encoding = "UTF-8", newline = "") as file: 
 
# counting the number of variables in the list 
    count = len(empty_list1) 
 
# using for loop with count and in enumerate empty list with an index of 0 to start 
for count, row in enumerate(empty_list1, start = 0): 
    # calculating the differences in amount between the indexes within the range 
    row = [int(empty_list1[value+1]) - int(empty_list1[value]) for value in range(len(empty_list2)-1)] 
 
# using for loop to find x in row 
    for x in row: 
 
# using if to check if x meets the conditions of <= 0 
        if row<=0: 
            if (row >= 0 for x in row): 
# using file.write to output if the condition is met 
                file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n") 
 
# assigning second condition if the condition above is not met 
            elif (x <= 0 for x in row): 
 
# using file.write to output if this condition is met 
                file.write(f"[CASH DEFICIT] DAY: {empty_list2[x.index(x)]} , AMOUNT: USD{round(abs(x))}\n")