import sqlite3

# Connect to database
# connRam - sqlite3.connect(':memory:') # Initialize database in memory, deletes after session terminates
conn = sqlite3.connect('App.db') # database by file

# Creates a cursor instance
cursor = conn.cursor()

# Create a Table
# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")

# DataTypes
    # NULL | INTEGER | REAL | TEXT | BLOB

# many_customers = [('Wes', 'Brown', 'wes@brown.com'),
#                  ('Steph', 'Kuewa', 'steph@kuewa.com'),
#                  ('Dan', 'Pas', 'dan@pas.com')]
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

cursor.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
cursor.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")

# Update a Record
cursor.execute("""UPDATE customers SET first_name = 'John'
                    WHERE ROWID = 1
""")

# Delete a Record
cursor.execute("DELETE FROM customers WHERE ROWID = 4")

# Order By
cursor.execute("SELECT ROWID, * ORDER BY ROWID DESC") # DESC --> High to Low
cursor.execute("SELECT ROWID, * ORDER BY last_name Desc") # DESC --> Z-->A


conn.commit()
# cursor.fetchone()
# cursor.fetchmany(3)
# print(cursor.fetchall())

cursor.execute("SELECT ROWID, * FROM customers")
items = cursor.fetchall() # returns a list of tuples

for item in items:
    print(item[0], " " + item[1] + " \t" + item[2])

# cursor.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")
# To execute cursor
conn.commit()

# Close our connection
conn.close()