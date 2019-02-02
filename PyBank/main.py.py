import os
import csv
import sys
filename  = open("pybank.txt",'w+')                     #this has python create a text file called pybank

csvpath = os.getcwd()                                   # Path to collect data from the main folder
filepath= os.path.join(csvpath, "Budget_data.csv")       # Path to collect the file of interest
prof_loss = 0
data = 0                                                #sets a bunch of variable parameters
average= 0
row_count= 0


with open(filepath, 'r') as csvfile:                       # reads the file as a csv
    
    
    csvreader = csv.reader(csvfile, delimiter=',')           # Split the data by commas
    next(csvreader)                                         # skips the header column of the row
    minval = []                                             # opens a list to hold all of the values for min and max
    maxval = []    
    for row in csvreader:                                   #cycles through the rows
        row_count += 1                                      # counts all of the rows
        prof_loss += int(row[1])                            # adds all of the values in column 2 together
        
        avg = int(prof_loss / row_count)                    #calculates the average
        minval.append(float(row[1]))                        # adds all of the values in row 1 to minval
        maxval.append(float(row[1]))
        highest = int(max(maxval))                          # finds max val of the list maxval and sets it to a variable
        lowest = int(min(minval))
        if int(row[1]) == int(highest):                     # finds the instance where the row equals the max value
            highdate = row[0]                               #outputs the corresponding date in the first column
        elif int(row[1]) == int(lowest):                    
            lowdate = row[0]  
    print("Financial Analysis")                             #following is a series of outputs for the terminal
    print("----------------------------------------------") #space holder for looks in the output
    print("Total Months: ",(row_count)) 
    print("Total: ", "$",(prof_loss))                       
    print("Average Change: ","$",(avg))
    print ("Greatest Increase in Profits: ", highest, "on", highdate)
    print ("Greatest Decrease in Profits: ", lowest, "on", lowdate)
    sys.stdout = filename                                   #this outputs all of the subsequent data to the txt file created earlier                              
    print("Financial Analysis")                             #there is probably a much more elegant solution but this works
    print("----------------------------------------------")
    print("Total Months: ",(row_count)) 
    print("Total: ", "$",(prof_loss))
    print("Average Change: ","$",(avg))
    print ("Greatest Increase in Profits: ", highest, "on", highdate)
    print ("Greatest Decrease in Profits: ", lowest, "on", lowdate)