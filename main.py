import sqlite3

conn = sqlite3.connect("test.db")

# Execute SQL statements and fetch resuults from SQL queries
cur = conn.cursor()
