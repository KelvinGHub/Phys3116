# This is a skeleton program for the computational assignment of PHYS3116
# As of 30 Sep we haven't decided which option we will undertake.
# function declaration
# These function declarations are just for the initial starting stubs.
# we may not necessaryly split our code contributions into these functions.
def  student_1():
    return
def student_2():
    return
def student_3():
    return
def read_data():
    f = open("demofile.txt")
    close(f)
    return
def starter():
    #open data file
    read_data()

# possible code that will be used in the assignment
# we have not yet decided which one to do, this will be done in week 3 meeting
import csv # import csv module to read csv files downloaded from moodle
def read_data():
    with open('data.csv', mode='r') as file: # open the file
        csvFile = csv.reader(file)
        for lines in csvFile: 
            print(lines)
    return 