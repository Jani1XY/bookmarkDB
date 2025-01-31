import sqlite3

db = sqlite3.connect("bookmarks.db")
c = db.cursor()

c.execute("""
            CREATE TABLE folders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parentID INTEGER,
                name TEXT NOT NULL
                ) STRICT
            """)

c.execute("""
            CREATE TABLE children(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parentID INTEGER NOT NULL,
            childID INTEGER NOT NULL,
            
            FOREIGN KEY(parentID) REFERENCES folders(id),
            FOREIGN KEY(childID) REFERENCES folders(id)
            ) STRICT
        """);

c.execute("""
            CREATE TABLE bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            link TEXT NOT NULL
            ) STRICT
            """)


db.commit()