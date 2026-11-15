import sqlite3

connection = sqlite3.connect("nexusops.db")
connection.execute("PRAGMA foreign_keys = ON")
print("NexusOps database connection successful!")

cursor = connection.cursor()

cursor.execute("""
    INSERT OR IGNORE INTO users (id, username, role)
    VALUES (?, ?, ?);
""", (1, 'analyst_anna', 'Analyst'))

cursor.execute("""
    INSERT OR IGNORE INTO incidents (id, name, severity, status, assigned_to)
    VALUES (?, ?, ?, ?, ?);
""", (
    1001, 'Suspicious Login', 'Medium', 'Open', 1
))

connection.commit()
print("NexusOps sample data seeded successfully!")

connection.close()