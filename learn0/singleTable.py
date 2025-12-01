import sqlite3 #Allows us to work with SQLite databases in Python

con = sqlite3.connect('database.db') #Establishes a connection to a SQL file which we named (database.db)
#The connect function returns a connection object that we can use to interact with database

con.execute('''CREATE TABLE Users (name TEXT, email TEXT)''')
#Creates a table named Users with 2 columns, name and email, and the statements are then executed by SQL

con.execute("INSERT INTO Users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com')) #Inserts a value into the table depending on the value given
con.execute("UPDATE Users SET name = ? WHERE email = ?", ('Jane Smith', 'john@example.com')) #Replaces a value with another
con.execute("DELETE FROM Users WHERE email = ?", ('john@example.com',)) #Deletes a value in the data

cursor = con.execute("SELECT * FROM Users")
for row in cursor:
    print(row)
#Retrieves all the values, the select * from selects all columns as well as the execute returning a cursor that we can iterate to retrieve data