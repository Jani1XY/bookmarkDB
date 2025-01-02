db = sqlite3.connect("bookmarks.db")
c = db.cursor()

c.execute("""
            CREATE TABLE hierarchy (
                id INT PRIMARY KEY,
                parentID INT NOT NULL,
                childrenID INT,
                name TEXT NOT NULL
                ) STRICT
            """)

c.execute("INSERT INTO hierarchy (id, parentID, name) VALUES (1, 0, 'root')")

db.commit()