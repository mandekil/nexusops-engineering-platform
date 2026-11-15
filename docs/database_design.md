## Purpose:
NexusOps needs persistent incident storage therefore there is database to be created. If there is no database, security analyst can only analyze the current incidents taken from the running program memory. When the program stops, the memory will be gone with the found incidents.

## Tables:
The database is built within two tables. Table users and incidents.
- **Table users** includes three columns: id, username, role.
- **Table incidents** includes five columns: id, name, severity, status, assigned_to.

## Relationship:
These two tables is connected using column assigned_to in table incidents references column id in table users. With the usage of foreign key, those two columns in different table can be connected.

## Database Workflow:
There are three Python files to run SQL program using sqlite3 packages: database_setup.py, database_seed.py, and database_query.py.
- **database_setup.py** is for creating tables.
- ***database_seed.py** is to insert and update data sample into the tables.
- **database_query.py** is to retrieve data from the tables row.

## Current Limitation:
Note that SQLite is being used for learning, PostgreSQL integration is planned and the schema is still a prototype.