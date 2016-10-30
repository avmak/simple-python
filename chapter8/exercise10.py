import sqlalchemy

conn = sqlalchemy.create_engine('sqlite:///books.db')
for row in conn.execute('SELECT title FROM books ORDER BY title'):
    print(*row)
