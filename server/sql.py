import sqlite3

db = sqlite3.connect("bookmarks.db", check_same_thread=False)
c = db.cursor()

def addBM(name, link, folder="root"):
    print("debug:: link "+str(link))
    print("debug:: name "+str(name))
    c.execute(f"INSERT INTO {folder} (name, link) VALUES (?, ?)", (name, link))
    db.commit()



def printRoot():
    c.execute("SELECT * FROM root")
    for i in c.fetchall():
        print(i)


def printHierarchy():
    c.execute("SELECT * FROM hierarchy")
    #print("id, pID, cID, name")
    for i in c.fetchall():
        print(i)