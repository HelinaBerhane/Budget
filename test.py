import sqlite3

con = sqlite3.connect( "budget.db" )
c = con.cursor()

c.execute( "CREATE TABLE IF NOT EXISTS income( date INT, amount FLOAT, notes STRING( 1000 ) )" )
c.execute( "INSERT INTO income VALUES ( '500', '22.4', 'blabllblbl' )" )

data = c.execute( "SELECT * FROM income" )

for i in data:
	print( i ) 

c.execute( "DELETE FROM income" )

con.commit()
con.close()