import sqlite3

sqlite_file = 'mytestDB'
table_name = 'my_table_3'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Retrieve column information
# Every column will be represented by a tuple with the following attributes:
# (id, name, type, notnull, default_value, primary_key)
c.execute('PRAGMA TABLE_INFO({})'.format(table_name))

# collect names in a list
names = [tup[1] for tup in c.fetchall()]
print(names)

# see the tup:
for tup in c.fetchall():
    print tup
# e.g., ['id', 'date', 'time', 'date_time']

# Closing the connection to the database file
conn.close()