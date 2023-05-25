#Data Base Inintializer
import sqlite3

#connect/create database
conn = sqlite3.connect('inventory.db')

#create a cursor to execute commands
curs = conn.cursor()

#create tables to hold our data
#curs.execute('CREATE TABLE weapons(name TEXT, attack INT, cost INT)')

#curs.execute('CREATE TABLE items(name TEXT, health INT, cost INT)')
#curs.execute('CREATE TABLE charms(name TEXT, cost INT)')


#insert data into our table
#curs.execute("INSERT INTO weapons VALUES('knife', 5, 10)")
#curs.execute("INSERT INTO weapons VALUES('sword', 10, 20)")
#curs.execute("INSERT INTO weapons VALUES('hammer', 20, 40)")

#curs.execute("INSERT INTO items VALUES('potion', 10, 10)")
#curs.execute("INSERT INTO items VALUES('steak', 15, 20)")
#curs.execute("INSERT INTO items VALUES('pizza', 25, 40)")

#drop a table
#curs.execute("DROP TABLE weapons")

#curs.execute("DELETE FROM items WHERE name = 'potion'")
#curs.execute("DELETE FROM charms")

#pull data from our table
# curs.execute("SELECT * FROM weapons")
# r1 = curs.fetchall()
# print(r1)

curs.execute("SELECT * FROM items")
r2 = curs.fetchall()
print(r2)

curs.execute("SELECT * FROM charms")
r3 = curs.fetchall()
print(r3)

#print our resluts in a neater format
# for i in results:
    # print(i)

#save and close database
conn.commit()
conn.close()
