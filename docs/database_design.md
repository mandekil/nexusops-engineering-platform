## Purpose:
NexusOps needs persistent storage so security analysts can retrieve and investigate incidents across application sessions. Without persistent storage, incident records held only in Python memory would be lost when the application stops.

## Tables:
The database is built within two tables. Table users and incidents.
- **Table users** includes three columns: id, username, role.
- **Table incidents** includes five columns: id, name, severity, status, assigned_to.

## Relationship:
The incidents.assigned_to column is a foreign key referencing users.id. One user can be assigned multiple incidents, while each incident can have at most one assigned user. With the usage of foreign key, those two columns in different table can be connected.

## Database Workflow:
There are three Python files to run SQL program using sqlite3 packages: database_setup.py, database_seed.py, and database_query.py.
- **database_setup.py** creates tables.
- ***database_seed.py** inserts sample users and incidents, ignoring records with existing primary keys.
- **database_query.py** retrieves data from the tables row.

## Current Limitation:
Note that SQLite is being used for learning, PostgreSQL integration is planned and the schema is still a prototype.