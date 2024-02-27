import sqlite3

connection = sqlite3.connect("Univer.db")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM Authors')
# for row in cursor.fetchall():
#     print(row)
#     print(row[1])

# print(cursor.fetchall())

cursor.execute("insert into Authors(FirstName, LastName) values ('test', 'test')")
connection.commit()

connection.close()
