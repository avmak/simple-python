# exercise 5

import csv
import sqlite3

books = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2007
Small Gods,Terry Pratchett,1992
'''

with open('books.csv', 'wt') as outf:
    outf.write(books)

# exercise 6

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
             (title TEXT, author TEXT, year INTEGER)''')
conn.commit()

# exercise 7

with open('books.csv', 'rt') as inf:
	rows_db = [(row['title'], row['author'], row['year']) for row in csv.DictReader(inf)]

ins_query = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
curs.executemany(ins_query, rows_db)
conn.commit()

# exercise 8

curs.execute('SELECT title FROM books ORDER BY title')
for row in curs.fetchall():
	print(row[0])

# exercise 9

for row in curs.execute('SELECT * FROM books ORDER BY year'):
	print(*row, sep=', ')
