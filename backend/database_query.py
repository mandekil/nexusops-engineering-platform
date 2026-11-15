import sqlite3

connection = sqlite3.connect("nexusops.db")
connection.execute("PRAGMA foreign_keys = ON")
print("NexusOps database connection successful!")

cursor = connection.cursor()

# Challenge 1: Retrieve all users
cursor.execute("""
    SELECT * FROM users;
""")
users = cursor.fetchall()

# Challenge 2: Retrieve all incidents
cursor.execute("""
    SELECT * FROM incidents;
""")
incidents = cursor.fetchall()

print("Users:", users)
print("Incidents:", incidents)

# BONUS CHALLENGE
cursor.execute("""
    SELECT * FROM incidents WHERE severity = 'Critical';
""")
critical_severity = cursor.fetchall()
print("Critical incidents:", critical_severity)

# Challenge 3: Retrieve incidents with assigned analysts
cursor.execute("""
    SELECT
        incidents.name,
        users.username
    FROM incidents
    JOIN users
        ON incidents.assigned_to = users.id;
""")
assigned_incidents = cursor.fetchall()
print("Assigned incidents:", assigned_incidents)

print("NexusOps data retrieved successfully!")

connection.close()