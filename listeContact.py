import sqlite3

conn = sqlite3.connect("contact.db")
cur = conn.cursor()

req = "SELECT * FROM contacts"
result = cur.execute(req)

for liste in result :
    print("Id :", liste[0])
    print("Nom :", liste[1])
    print("Prenom :", liste[2])
    print("Email :", liste[3])
    print("Telephone :", liste[4])
    print("Adresse :", liste[5])
