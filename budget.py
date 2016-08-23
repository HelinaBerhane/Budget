# This Python file uses the following encoding: utf-8
import time

### Functions and Constants ###

# convert d/m/y to unix time

UnixYear = 31557600

def toUnix(date):
    return time.mktime(time.strptime(date, '%d/%m/%Y'))
        # time.strptime takes a string and turns it into a time object
            # https://docs.python.org/2/library/time.html#time.strftime
        # time.mktime turns the time object into unix time

'''    
# convert unix time to d/m/y
def toDate(Udate):
    # find a way to do this
'''
        
# convert a float to currenct in GBP
def toPounds(money):
    string = (str("£") + str(round(money,2)))
    return string

### Income ###

# test
print("£")

# create an array to hold the sources of income
masterIncome = []

# ask if they have any income
initialQuestion = raw_input("do you have any income (y/n)?")
# look up how to catch invalid inputs

# if they have an income
if initialQuestion == "y":
    
    # ask how much
    incomeStr = raw_input("Input amount, start, info")
    incArr = incomeStr.split(", ")
    
    # log the amount, daily amount, start date, end date and info
    fixedIncomeArr = [toPounds(float(incArr[0])), toPounds(float(incArr[0])/365.25), toUnix(incArr[1]), toUnix(incArr[1])+UnixYear, incArr[2]]
    masterIncome.append(fixedIncomeArr)
    
    # ask if they have any more income until they say no
    while True:
        question = raw_input("do you have any other sources of income (y/n)?")
        
        # if they have other sources of income
        if question == "y":
            
            # ask how much
            nIncomeStr = raw_input("Input amount, start, info")
            nIncArr = nIncomeStr.split(", ")
            
            # log the amount, daily amount, start date, end date and info
            nFixedIncArr = [toPounds(float(nIncArr[0])), toPounds(float(nIncArr[0])/365.25), toUnix(nIncArr[1]), toUnix(nIncArr[1])+UnixYear, nIncArr[2]]
            masterIncome.append(nFixedIncArr)
            # beware, python doesnt like printing £ signs in arrays
        
        elif question == "n":
            for i in masterIncome:
                print("total:" + i[0] + ", " + "daily:" + i[1] + ", " + "start:" + str(i[2]) + ", " + "end:" + str(i[3]) + ", " + "info:" + i[4])
            break

### Spendings ###

'''
masterSpend = []

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