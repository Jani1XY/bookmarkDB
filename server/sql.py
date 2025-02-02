import sqlite3

db = sqlite3.connect("bookmarks.db", check_same_thread=False)
c = db.cursor()

def addBM(name, link, folder=""):
    try:
        c.execute("INSERT INTO bookmarks (name, link) VALUES (?, ?)", (name, link))
        db.commit()
        printBookmarks()
        return True
    
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False


def getLink(url):
    try:
        c.execute("SELECT link FROM bookmarks WHERE link=?",(url,))
        fetched = c.fetchone()
        if fetched == None:
            return False

        if fetched[0] == url:
            return True
        
        return False

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False


def deleteOneLink(url):
    try:
        c.execute("DELETE FROM bookmarks WHERE link=?",(url,))
        db.commit()
        print("Deleted from database: "+url)

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False


def printBookmarks():
    c.execute("SELECT * FROM bookmarks")
    for i in c.fetchall():
        print(i)


def printFolders():
    c.execute("SELECT * FROM folders")
    #print("id, pID, cID, name")
    for i in c.fetchall():
        print(i)


if __name__ == '__main__':
    printBookmarks()