import sqlite3

conn = sqlite3.connect("contact.db")
cur = conn.cursor()

req = "SELECT * FROM contacts WHERE telephone = 777998866"
result = cur.execute(req)

for cont in result :
    print("Le contact selectionne est:", cont)
    
