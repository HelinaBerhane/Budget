### To Do ###

# []	replace time with datetime 				https://docs.python.org/2/library/datetime.html
# []	fix toDate						http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python

Modules
time	    - convert between unix time and d/m/y formats
sqlite3     - databases
                -- https://docs.python.org/2/library/sqlite3.html
                -- http://www.w3schools.com/sql/

Functions
toUnix - convert from dd/mm/yyyy to unix time
toDate - convert from unix time to dd/mm/yyyy


---- TO DO ----
ask the user what they want to do (print this key):
    1 to add a source of income
    2 to add a spending
    3 to add an impulse buy
    4 to see graphs
        4.1 graphs about income
            4.1.1 total current daily income
            4.1.2 income over time
            4.1.3 current income from different sources
            4.1.4 total income from different sources
        4.2 graphs a

1 if they want to add a source of income:
    make an income table if there isnt one already
    ask them for the start date, amount and any notes
    calculate the daily amount
    add the income to the table

2 if they want to add a spending:
    make a spendings table if there isnt one already
        (category, start date, end date, amount, notes)
    ask them for the category, start date, end date, amount and any notes
        the category should be picked from a predefined list
            1 tech
            2 holidays
            3 presents
            4 etc.
    calculate the daily amount
    add the spending to the table

3 if they want to log an impulse spend:
    make a spendings table if there isnt one already
    

4.1.1 if they want to see the current total income:
    sort through the income table to see all elements with a start date within the last year
    sum the daily amount column
    print the result
    



if they want to add
#first, assume you have an income of £x

'''def toUnix( dateTime ):
    
    return time.mktime( time.strptime( dateTime, '%d/%m/%Y' ) )

def newSaveItem( info, start, end, price, priority ):
    saveList = getCurrentSaves()
    budget = getCurrentBudget()
    
    curtime = time.time()
    startUnix = toUnix( start )
    endUnix = toUnix( end )
    
    totalDays = ( endUnix - startUnix ) / ( 3600 * 24 )
    pricePerDay = price / totalDays
    
    newBudget = budget - pricePerDay'''

#ask if they 
'''print("add a spending? (y/n)")'''

#if yes, ask for the details


'''spend1 = [ "start", "staasdauvfgsyrt", 5, [56] ]'''
# arrays keep order and values
# you need to refer to the thing by number (starting from 0)

'''CompParts = 

dic = { "start": 5, "end": 6 }'''
#dictionaries dont maintain order, but they'll maintain value
# you can refer to the thing with a label

'''start = spend1[3][0]
print(start)
start = dic["start"]'''


# warnings
    # every day, you should have a warning

# Income
    # each source of money should be considered separately
    # how much was earned yearly, monthly and daily should be calculated
        # this should be averaged over the last period (if you've been working for that long) or predicted
    # each payment should be logged
    # each time you get any money
        # it should be distributed across the next year and used for savings
        
    

# Spending
    
    # types
        # each spending should be given a type for graphing / predicting purposes
        # the amount spent in each category should be summed and used to predict spending patterns
    
    # for impulsive spending, some money should be set aside in separate pots
        # i.e. £x a day for clothes, £y a day for food
        # the amount set aside for each thing should be based on the p
        # alternatively, you could just spend impulsively
            # whatever you spent will be taken out of the savings for other purchases
            # how much is taken out of the different spendings could be based on their priorities
            # things with an end date should not be affected by this
                #or if they are, they should take more from the budget for every day remaining
        # every time you deduct something, it should output a list of things that would be affected
            # e.g. because you bought this, buying something else will take x days longer
            # if the changes are accel

    # each purchase would have a priority
        # e.g. necessary food would have the highest priority 
        # a lower priority number would have a lower priority
        # things with a 
        # you should have some way to rescale priorities
            # i.e. add a new priority in between already set priorities
            # multiply all priorities by a number
    
    # recurring spendings
    
    # completed spendings
        # each task should have a status
            # e.g. saving, saved, bought, redistributed
            # the user should be able to change this at any point (one way)
            # if the user decides to go from saving to bought
                # the app should warn them that they haven't finished saving for the item
                # if they still want to buy it, the app should ask how much was spent
                # the amount already saved for the item should be deducted
                # the difference should be redistributed to/from the other savings (based on priority)
            # every time something is bought, the user should be asked how much was spent and the difference should be redistributed
            # redistributed spendings should be counted as having £0 saved
                #so if you want to start saving again, you start from scratch

# logging
    # income
        # there should be a log of all pyments, who they were from and why they were given
            # e.g. £x from Spero for assisting for y hours
    # completed spendings
        # you should have a list of all of the things that have been saved for and their status'
        
# graphs
    # the amount spent in each category should be shown in a pi chart
