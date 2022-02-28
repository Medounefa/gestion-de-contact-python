import sqlite3

conn = sqlite3.connect("contact.db")
cur = conn.cursor()

# utiliser avec les variable
nom = input("Entrez votre nom")
prenom = input("Entrez votre prenom")
email = input("Entrez votre email")
telephone = int(input("Entrez votre numero de telephone"))
adresse = input("Entrez votre adresse")

req = "insert into contacts (nom, prenom, email, telephone, adresse) values (?, ?, ?, ?,?)"
# req = "create table contacts(id integer primary key autoincrement, nom text, prenom text, email text, telephone integer, adresse text)"
cur.execute(req, (nom, prenom, email, telephone, adresse))

conn.commit()
conn.close()