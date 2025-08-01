import numpy as np
import pandas as pd
from datetime import date
import sqlite3 as sql

from esg import FlatRateESG

print("hello world")

# Creating bond and liabilities classes

class Bond:
    def __init__(self, id, name, face, coupon, maturity):
        self.id = id
        self.name = name
        self.face = face
        self.coupon = coupon
        self.maturity = maturity


class Liability:
    payment_amount = 0
    payment_duration = 0 # This is supposed to be how long in years the payments will be occuring for


# Discount rate function assumes annual compounding
# Following formula DR = (1 + r)^-t
def discount_rate(delta_t, rate):
    DR = 1 + rate
    DR = (DR ** (-1*delta_t))
    return DR

def present_value(future_cash_flows):
    # Creates an array of the future cash flows, with each of the values changed to represent their current values
    discounted_cash_flows = []
    for i in range(len(future_cash_flows)):
        discounted_cash_flows.append( discount_rate(i, 0.03) * future_cash_flows[i])
    # Summing to find the total current value of the future cash flow
    total_cash = 0
    for i in discounted_cash_flows:
        total_cash += i

    return total_cash


# Creating the database
def sql_database_setup():
    conn = sql.connect('alm.db')
    cursor = conn.cursor()


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
    conn.close()

# Inserting bonds into our previously created database
def inserting_bonds():
    conn = sql.connect('alm.db')
    cursor = conn.cursor()

    # sample bond info
    bonds = [
        (1, 'bond 1', 1000, 0.05, 10),
        (2, 'bond 2', 2000, 0.15, 15),
        (3, 'bond 3', 1500, 0.03, 8),
        (4, 'bond 4', 1250, 0.05, 11),
        (5, 'bond 5', 1300, 0.07, 13),
    ]

    # Actually putting all the bonds into the db
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

    conn.close()
    return bond_list

def liability_array_setup(amount, length):
    liab = []
    for i in range(length):
        liab.append(amount)
    return np.array(liab)




####################################################################### TESTING TESTING TESTING


if __name__ == "__main__":
    future_cash_flows = [10000, 10000, 10000] # can possible change to numpy array
    print(present_value(future_cash_flows))

    # The following two functions create our sql database and insert our bonds into it
    sql_database_setup()
    inserting_bonds()
    # The next function pulls the bond portfolio from the sql database and stores them in an array
    bond_portfolio = bond_portfolio_creation()

    liability_amount = int(input("How large is the liability payment? "))
    liability_length = int(input("How long will your liability be paid out for (years)? "))

    esg = FlatRateESG(0.03)
    print(esg.generate(5, liability_length))

    liabilities = liability_array_setup(liability_amount, liability_length)
    print(present_value(liabilities))