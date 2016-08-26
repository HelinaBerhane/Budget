# This Python file uses the following encoding: utf-8
import time    # time
import sqlite3 # databases

### Functions and Constants ###

unixYear  = 31557600
unixMonth = 2629800
unixDay   = 86400

# convert d/m/y to unix time
def toUnix(date):
    return time.mktime(time.strptime(date, '%d/%m/%Y'))
        # time.strptime takes a string and turns it into a time object
            # https://docs.python.org/2/library/time.html#time.strftime
        # time.mktime turns the time object into unix time
 
# convert unix time to d/m/y
def toDate(uDate):
    years  = round(uDate/unixYear,0)
    months = round((uDate%unixYear)/unixMonth,0)
    days   = round((uDate%unixMonth)/unixDay,0)
    return str(int(years)) + "/" + str(int(months)) + "/" + str(int(days))
    # broken
        
# convert a float to currenct in GBP
def toPounds(money):
    string = (str("£") + str(round(money,2)))
    return string

### Income ###

# initialise the master arrays
masterIncome = []
masterSpend  = []  # not used at the moment

# ask if they have any income
initialQuestion = raw_input("do you have any income (y/n)?")
# look up how to catch invalid inputs

# if they have an income
if initialQuestion == "y":
    
    # ask how much
    incomeStr = raw_input("Input amount, start, info")
    incArr    = incomeStr.split(", ")
    
    # log the amount, daily amount, start date, end date and info
    fixedIncomeArr = [float(incArr[0]), float(incArr[0])/365.25, toUnix(incArr[1]), toUnix(incArr[1])+unixYear, incArr[2]]
    
    masterIncome.append(fixedIncomeArr)
    
    # ask if they have any more income until they say no
    while True:
        question = raw_input("do you have any other sources of income (y/n)?")
        
        # if they have other sources of income
        if question == "y":
            
            # ask how much
            nIncomeStr = raw_input("Input amount, start, info")
            nIncArr    = nIncomeStr.split(", ")
            
            # log the amount, daily amount, start date, end date and info
            nFixedIncArr = [float(nIncArr[0]), float(nIncArr[0])/365.25, toUnix(nIncArr[1]), toUnix(nIncArr[1])+unixYear, nIncArr[2]]
            masterIncome.append(nFixedIncArr)
            # beware, python doesnt like printing £ signs in arrays
        
        else:
            for i in masterIncome:
                incomeSum = 0
                print("total:" + toPounds(i[0]) + ", " + "daily:" + toPounds(i[1]) + ", " + "start:" + toDate(i[2]) + ", " + "end:" + toDate(i[3]) + ", " + "info:" + i[4])
                incomeSum = incomeSum + i[1]
            print("Sum: " + toPounds(incomeSum))
            break
            

### Spendings ###

'''

while True:
    question = raw_input("Do you want to add a spending (y/n)?")
    
    if question == "y":
        array = raw_input("Input start, end, info")
        arraye = array.split(", ")
        
        spend1 = [toUnix(arraye[0]), toUnix(arraye[1]), arraye[2]]
        masterSpend.append(spend1)
        
    elif question == "n":
        print(masterSpend)
        break
'''

