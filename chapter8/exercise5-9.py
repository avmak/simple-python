# exercise 5

books = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2007
Small Gods,Terry Pratchett,1992
'''

with open('books.csv', 'wt') as outf:
    outf.write(books)

# exercise 6

import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
             (title TEXT, author TEXT, year INTEGER)''')
conn.commit()
