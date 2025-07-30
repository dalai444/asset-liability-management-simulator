import numpy as np
import pandas as pd
from datetime import date
import sqlite3 as sql

print("hello world")

# Creating bond and liabilities classes

class Bond:
    def __init__(self, n, f, c, q, m):
        self.name = n
        self.face = f
        self.coupon = c
        self.freq = q
        self.maturity = m

        


class Liabilities:
    payment_amount = 0
    payment_duration = 0 # This is supposed to be how long in years the payments will be occuring for



# Trying to code the sql server to host the bond information





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
        (1, 'bond 2', 2000, 0.15, 15),
        (1, 'bond 3', 1500, 0.03, 8),
        (1, 'bond 4', 1250, 0.05, 11),
        (1, 'bond 5', 1300, 0.07, 13),
    ]

    conn.commit()
    conn.close()

####################################################################### TESTING TESTING TESTING


if __name__ == "__main__":
    future_cash_flows = [10000, 10000, 10000]
    print(present_value(future_cash_flows))

    sql_database_setup()
    inserting_bonds()

    