import sqlite3

conn=sqlite3.connect('test.db')

c=conn.cursor()

c.execute("CREATE TABLE BOOKRE(\
ID INTEGER PRIMARY KEY AUTOINCREMENT,\
NAME TEXT,\
AUTHOR TEXT,\
GENRE TEXT,\
USERID INTEGER\
)")