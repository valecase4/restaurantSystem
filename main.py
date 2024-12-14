import sqlite3

conn = sqlite3.connect("test.db")

# Execute SQL statements and fetch resuults from SQL queries
cur = conn.cursor()

# cur.execute("DROP TABLE reservations")

# Create a table for reservations
cur.execute("CREATE TABLE IF NOT EXISTS reservations(id, booking_date, booking_time, name, phone_number, people_number)")
