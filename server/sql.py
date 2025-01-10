import sqlite3

db = sqlite3.connect("bookmarks.db", check_same_thread=False)
c = db.cursor()

def addBM(name, link, folder="root"):
    try:
        c.execute(f"INSERT INTO {folder} (name, link) VALUES (?, ?)", (name, link))
        db.commit()
        return True
    
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False



def printRoot():
    c.execute("SELECT * FROM root")
    for i in c.fetchall():
        print(i)


def printHierarchy():
    c.execute("SELECT * FROM hierarchy")
    #print("id, pID, cID, name")
    for i in c.fetchall():
        print(i)


if __name__ == '__main__':
    printRoot()