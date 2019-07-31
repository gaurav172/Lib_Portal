import sqlite3


with sqlite3.connect('test.db') as conn: 
	c=conn.cursor()
	c.execute('''INSERT INTO USER(FIRSTNAME,LASTNAME,USERNAME,PASSWORD,EMAIL,TYPE)VALUES(?,?,?,?,?,?)''',("admin","","admin","admin","admin@lib.com","admin"))
	conn.commit()

