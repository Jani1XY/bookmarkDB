import sqlite3

db = sqlite3.connect("bookmarks.db")
c = db.cursor()

c.execute("""
            CREATE TABLE hierarchy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parentID INT NOT NULL,
                childrenID INT,
                name TEXT NOT NULL
                ) STRICT
            """)

c.execute("INSERT INTO hierarchy (id, parentID, name) VALUES (1, 0, 'root')")

c.execute("""
            CREATE TABLE root (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            link TEXT NOT NULL
            ) STRICT
            """)


db.commit()