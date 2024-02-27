import sqlite3

connection = sqlite3.connect("Books.db")

cursor = connection.cursor()
cursor.execute('SELECT Pages, Price FROM Books')
pages, price = 0, 0
for row in cursor.fetchall():
    pages += row[0]
    price += row[1]
print(f'Total num of pages - {pages}\n'
      f'Total price - {price}')

connection.close()
