import sqlite3

def get_reservations_data(db):
    """
    Get reservations data from database
    """

    data = []

    conn = sqlite3.connect(db)
    cur = conn.cursor()

    reservations = cur.execute("SELECT * FROM reservations")

    for row in reservations.fetchall():
        reservation = {}

        reservation['ID'] = row[0]
        reservation['Booking Date'] = row[1]
        reservation['Booking Time'] = row[2]
        reservation['Booking Name'] = row[3]
        reservation['Phone Number'] = row[4]
        reservation['People Number'] = row[5]
        reservation["Edit"] = ""
        reservation["Delete"] = ""

        data.append(reservation)

    return data


