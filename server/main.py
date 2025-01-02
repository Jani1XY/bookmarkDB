import sqlite3

db = sqlite3.connect("bookmarks.db")
c = db.cursor()




c.execute("SELECT * FROM hierarchy")
#print("id, pID, cID, name")
for i in c.fetchall():
    print(i)