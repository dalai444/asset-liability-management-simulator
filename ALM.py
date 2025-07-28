import numpy as np
import pandas as pd
from datetime import date
import sqlite3 as sql

print("hello world")

# Creating bond and liabilities classes

class bond:
    def __init__(self, n, f, c, q, m):
        self.name = n
        self.face = f
        self.coupon = c
        self.freq = q
        self.maturity = m

        


class liabilities:
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






####################################################################### TESTING TESTING TESTING

future_cash_flows = [10000, 10000, 10000]
print(present_value(future_cash_flows))
