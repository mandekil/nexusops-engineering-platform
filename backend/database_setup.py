import sqlite3

connection = sqlite3.connect("nexusops.db")
connection.execute("PRAGMA foreign_keys = ON")
print("NexusOps database connection successful!")

cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        role VARCHAR(30) NOT NULL
    );
""")

cursor.execute("""

   CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        severity VARCHAR(20) NOT NULL,
        status VARCHAR(30) NOT NULL,
        assigned_to INTEGER,
        FOREIGN KEY (assigned_to) REFERENCES users(id)
    );
""")

connection.commit()
print("NexusOps database tables created successfully!")

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")
print("Database tables:", cursor.fetchall())

connection.close()