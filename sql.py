#

import sqlite3

with sqlite3.connect('blog.db') as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE posts (title TEXT,post TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good","Excellent")')
    c.execute('INSERT INTO posts VALUES("Bad","Very bad")')
    c.execute('INSERT INTO posts VALUES("Awful","Terrible")')



