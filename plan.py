
Modules you need to import:
time	- to convert between unix time and d/m/y formats
sqlite3 - to use a database to store data locally
	  -- what was the difference between information and data again?

Using sqlite3:
- to use sqlite3, you need to make a Connection object that represents the database.
  -- conn = sqlite3.connect('budget.db')
  -- A SQLite database connection has the following attributes and methods (some not included):
     --- isolation_level			gets or sets the current isolation level.
     --- cursor([cursorClass])			The cursor method accepts a single optional parameter cursorClass.
     --- commit()				This method commits the current transaction.
						If you don’t call this method, anything you did since the last call to commit() is not visible from other database connections.
						If you wonder why you don’t see the data you’ve written to the database, please check you didn’t forget to call this method.
     --- rollback ()                            This method rolls back any changes to the database since the last call to commit().
     --- close()                                This closes the database connection.
						Note that this does not automatically call commit().
						If you just close your database connection without calling commit() first, your changes will be lost!
     --- execute(sql[, parameters])             This is a nonstandard shortcut that creates an intermediate cursor object by calling the cursor method, then calls the cursor’s execute method with the parameters given.
     --- executemany(sql[, parameters])
     --- executescript(sql_script)
     --- create_function(name, num_params, func)
- the data will be stored in budget.db

''''''



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