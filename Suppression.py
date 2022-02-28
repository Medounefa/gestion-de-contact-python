import sqlite3

conn = sqlite3.connect("contact.db")
cur = conn.cursor()

req = "DELETE FROM contacts WHERE id = 3"
cur.execute(req)
conn.commit()
cur.close()
conn.close()
