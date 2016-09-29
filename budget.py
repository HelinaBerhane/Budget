# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases

#--------------------#
#-- Initialisation --#
#--------------------#

# create the connection object that represents the database
connection = sqlite3.connect('budget.db')
# create a Cursor object and call its execute() method to perform SQL commands:
c = connection.cursor()
# Create the tables
c.execute("CREATE TABLE IF NOT EXISTS incomeTable(date INT, amount FLOAT, dailyAmount FLOAT, notes STRING(1000))")
c.execute("CREATE TABLE IF NOT EXISTS spendingTable(date INT, amount FLOAT, notes STRING(1000))")

#---------------#
#-- Functions --#
#---------------#

def incomeFunction():
    # Ask them to input their income
    iStr    = input("Input date, amount, notes")
    iArr    = iStr.split(", ")
    fIArr   = [iArr[0], iArr[1], str(float(iArr[1])/365), iArr[2]]
    c.execute("INSERT INTO incomeTable VALUES (?,?,?,?)", fIArr)
    connection.commit()
    
    # Ask if they want to add more sources of income
    while True:
        questionI = input("Do you want to add any more sources of income? y/n")
        if QuestionI == "y":
            # Add income
            iStr    = input("Input date, amount, notes")
            iArr    = iStr.split(", ")
            fIArr   = [iArr[0], iArr[1], str(float(iArr[1])/365), iArr[2]]
            c.execute("INSERT INTO incomeTable VALUES (?,?,?,?)", fIArr)
            connection.commit()
        else:
            # Print sources of income
            print("Your sources of income are:")
            for row in c.execute("SELECT * FROM incomeTable"):
	        print(row)
            # Print total daily income
            c.execute("SELECT SUM(dailyAmount) FROM incomeTable")
            dailySumI = c.fetchone()
            print("Your total daily income is " + str(dailySumI[0]))
            break

def spendingFunction():
    # Ask them to input their spending
    sStr    = input("Input date, amount, notes")
    sArr    = sStr.split(", ")
    fSArr   = [sArr[0], sArr[1], str(float(sArr[1])/365), sArr[2]]
    c.execute("INSERT INTO spendingTable VALUES (?,?,?,?)", fSArr)
    connection.commit()
    
    # Ask if they want to add more sources of income
    while True:
        questionS = input("Do you want to add any more spendings? y/n")
        if questionS == "y":
            # Add spending
            sStr    = input("Input date, amount, notes")
            sArr    = iStr.split(", ")
            fSArr   = [sArr[0], sArr[1], str(float(sArr[1])/365), sArr[2]]
            c.execute("INSERT INTO spendingTable VALUES (?,?,?,?)", fSArr)
            connection.commit()
        else:
            # Print sources of income
            print("Your sources of spending are:")
            for row in c.execute("SELECT * FROM spendingTable"):
	        print(row)
            # Print total daily income
            c.execute("SELECT SUM(dailyAmount) FROM spendingTable")
            dailySumS = c.fetchone()
            print("Your total daily spending is " + str(dailySumS[0]))
            break

#---------------#
#-- Questions --#
#---------------#

# ask the user what they want to do
print("what do you want to do?")
print("    1 to add a source of income")
print("    2 to add a spending")
print("    3 to add an impulse buy")
print("    4 to see graphs")
print("        4.1 graphs about income")
print("            4.1.1 total current daily income")
print("            4.1.2 income over time")
print("            4.1.3 current income from different sources")
print("            4.1.4 total income from different sources")
intQ = input("        4.2 graphs about spendings")

while True:
    # if they want to add a source of income
    if intentionQuestion == 1:
        incomeFunction()
        break
    
    # if they want to add a spending
    elif intentionQuestion == 2:
        spendingFunction()
        break
    
    # if they want to add an impulse buy
    elif intentionQuestion == 3:
        break
    
    # if they want to see graphs
    elif intentionQuestion == 4: 
	# ask them what graphs they want to see
        print("what graphs do you want to see?")
	print("    1 graphs about income")
	print("        1.1 total current daily income")
	print("        1.2 income over time")
	print("        1.3 current income from different sources")
	intQ4 = input("        1.4 total income from different sources")
   	    # if they want to see graphs about income
            if intQ4 == 1:
                # ask them what graphs they want to see
                # if they want to see graphs about 
                if intQ4 == 

                # if they want to see graphs about 
                if intQ4 == 

                # if they want to see graphs about 
                if intQ4 == 
        break
    else:
	break

#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
