# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases

#----------------------------------------------------------------------------------------------------------------------------#
### Initialisation ###

# create the connection object that represents the database
connection = sqlite3.connect('budget.db')
# create a Cursor object and call its execute() method to perform SQL commands:
c = connection.cursor()

## In ##
# Create the income table
c.execute("CREATE TABLE IF NOT EXISTS incomeTable(date INT, amount FLOAT, dailyAmount FLOAT, notes STRING(1000))")

# Ask to add income
askI = input("Do you want to add any incomes? y/n")
# Add income
if askI == "y":
    iStr    = input("Input date, amount, notes")
    iArr    = iStr.split(", ")
    fIArr   = [iArr[0], iArr[1], str(float(iArr[1])/365), iArr[2]]
	#iDate   = iArr[0]
	#iAmount = iArr[1]
	#iDaily  = str(float(iAmount)/365.25)
	#iNotes  = incArr[2]
    c.execute("INSERT INTO incomeTable VALUES (?,?,?,?)", fIArr)
    # this doesnt work atm
# Print incomeTable
for row in c.execute("SELECT * FROM incomeTable"):
	print( row )

## Out ##
# Create the spendings table
#c.execute("CREATE TABLE IF NOT EXISTS spendingTable(date INT, amount FLOAT, notes STRING(1000))")
# Ask to add spendings
#askSpendings = input("Do you want to add any spendings? y/n")
# Add income
#if askSpendings == "y":
    #spendingsStr = input("Input date, amount, notes")
    #spendArr     = spendingsStr.split(", ")
    #c.execute("INSERT INTO spendings (date, amount, notes) VALUES ("+incArr[0]+", "+incArr[1]+", "+incArr[2]+")") 
    # this doesnt work atm
# Print incomeTable
#spendingsData = c.execute( "SELECT * FROM spendings" )
#for i in data:
#	print( i )
	
# Insert a row of data:         c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes:    conn.commit()

# open the database


# load the incomes and list them

# ask the user if they want to add any new incomes

# load the spendings and list them

# ask the user if they want to add any new spendings



            
#----------------------------------------------------------------------------------------------------------------------------#
### End ###

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
