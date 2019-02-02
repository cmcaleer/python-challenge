import os
import csv
import sys

filename  = open("pyPoll.txt",'w+')                     #will edit or create a new txt file called pyPoll
tally = 0                                               #sets the variable tally to 0 to define it
csvpath = os.getcwd()                                   # Path to collect data from the main folder
filepath= os.path.join(csvpath, "election_data.csv")    #opens the specific folder of interest


with open(filepath, 'r') as csvfile:                       # reads the file as a csv
    csvreader = csv.reader(csvfile, delimiter=',')           # Split the data by commas
    next(csvreader)                                        #ignores the header columns
    vote_counts = {}                                        #starts a dictionary that we will add the new candidate names and votes to
    for row in csvreader:                                   #cycles through the rows
        tally += 1                                          #counts all of the votes cast 
        this_name = row[2]                                  #sets a variable that will pull dat from column 3
        if this_name not in vote_counts.keys():             # if a name is not already in the dictionary it will add it 
            vote_counts[this_name] = 1                      #and add one to its counter
        else:
            vote_counts[this_name] += 1                     #if it is already there it adds one to the counter
    del(vote_counts[""])                                    #deletes any key in the dictionary that was a no vote
    print("-----------------------------")                  #for formatting 
    print("Total Votes Cast: ", tally)
    print("-----------------------------")   
    for key,value in vote_counts.items():                   #this will run through the key:value pairs 
        print(key,":", '{0:.02%}'.format(value/(tally)), value, "votes" )  #print the key the value and the % formatted as a two digit decimal 
    print("-----------------------------")
    print("The winner is: ",  max(vote_counts, key=lambda i: vote_counts[i]))       # key lambda i vote_counts [i] searches the values for the designated function(max) 
                                                                                    #in the desired directory and outputs the associated key
    sys.stdout = filename                                                           #writes to the txt file created earlier
    print("-----------------------------") 
    print("Total Votes Cast: ", tally)
    print("-----------------------------")   
    for key,value in vote_counts.items():
        print(key,":", '{0:.02%}'.format(value/(tally)), value, "votes" ) 
    print("The winner is: ",  max(vote_counts, key=lambda i: vote_counts[i]))   
        



