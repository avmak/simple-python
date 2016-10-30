# exercise 3

books = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('books.csv', 'wt') as outf:
    outf.write(books)


# exercise 4

import csv

with open('books.csv', 'rt') as inf:
    for row in csv.DictReader(inf):									# output: {'author': 'J R R Tolkien', 'book': 'The Hobbit'}
		print(row)										# output: {'author': 'Lynne Truss', 'book': 'Eats, Shoots & Leaves'}
