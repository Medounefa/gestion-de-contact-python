import sqlite3

conn = sqlite3.connect("contact.db")
cur = conn.cursor()

req = "update contacts set telephone=772333333 where id = 3"
cur.execute(req)
conn.commit()
conn.close()

