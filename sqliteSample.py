#sqlite build sample
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS foods')

c.execute('''CREATE TABLE foods (name text, qty real, cost int)''')

c.execute('''INSERT INTO foods VALUES ('sandwich', 30.14, 20)''')

c.execute('SELECT * FROM foods')

print c.fetchone()

conn.commit()
conn.close()
