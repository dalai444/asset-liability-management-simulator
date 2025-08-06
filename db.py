import sqlite3 as sql
from bond import Bond

# Creating the database
def sql_database_setup():
    conn = sql.connect('alm.db')
    cursor = conn.cursor()

    # Creating the sql table with columns: bond_id, name, face_value, coupon_rate, and maturity_years
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bonds (
            bond_id INTEGER PRIMARY KEY,
            name TEXT,
            face_value REAL,
            coupon_rate REAL,
            maturity_years INTEGER
        )
    ''')

    conn.commit()
    conn.close() # Saving and closing our database

# Inserting bonds into our previously created database
def inserting_bonds():
    conn = sql.connect('alm.db')
    cursor = conn.cursor()

    # sample bond info
    bonds = [
        (1, 'bond 1', 45000, 0.025, 30),
        (2, 'bond 2', 60000, 0.035, 10),
        (3, 'bond 3', 67500, 0.04, 20),
        (4, 'bond 4', 56250, 0.05, 30),
        (5, 'bond 5', 50500, 0.045, 20),
    ]

    # Actually inserting all the bonds into the db
    cursor.executemany('''
            INSERT OR REPLACE INTO bonds (bond_id, name, face_value, coupon_rate, maturity_years)
            VALUES (?, ?, ?, ?, ?)
        ''', bonds)

    conn.commit()
    conn.close() # Saving and closing

# This function accesses the database and returns the bonds in an array of Bond objects
def bond_portfolio_creation():
    conn = sql.connect('alm.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bonds") # SQL command to get the whole table
    rows = cursor.fetchall()

    # For each row in the table
    # Create a Bond object and add it to an array of bonds
    bond_list = []
    for row in rows:
        bond = Bond( # Creating a bond object
            id=row[0],
            name=row[1],
            face=row[2],
            coupon=row[3],
            maturity=row[4]   # Coordinates each value stored in db to constructor parameter of Bond class.
        )
        bond_list.append(bond) 

    conn.close() # Close the database after extracting all values
    return bond_list # Return our array of bonds (the bond portfolio)
