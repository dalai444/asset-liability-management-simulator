import numpy as np
import pandas as pd
from datetime import date
import sqlite3 as sql
import matplotlib.pyplot as plt

from esg import StochasticRateESG
from asset import bond_cashflows
from db import sql_database_setup, inserting_bonds, bond_portfolio_creation
from graph import visualizing_data

print("hello world")

# Creating bond and liabilities classes

class Liability:
    payment_amount = 0
    payment_duration = 0 # This is supposed to be how long in years the payments will be occuring for


# Discount rate function assumes annual compounding
# Following formula DR = (1 + r)^-t
def discount_rate(delta_t, rate):
    DR = 1 + rate
    DR = (DR ** (-1*delta_t))
    return DR

def present_value_flat(future_cash_flows):
    # Creates an array of the future cash flows, with each of the values changed to represent their current values
    discounted_cash_flows = []
    for i in range(len(future_cash_flows)):
        discounted_cash_flows.append( discount_rate(i, 0.03) * future_cash_flows[i])
    # Summing to find the total current value of the future cash flow
    total_cash = 0
    for i in discounted_cash_flows:
        total_cash += i

    return total_cash

def present_value_stochastic(future_cash_flows, rate_path):
    pv = sum(cf * (1 + r)**(-t) 
         for t, (cf, r) in enumerate(zip(future_cash_flows, rate_path), start=1))
    return pv


def liability_array_setup(amount, length):
    liab = []
    for i in range(length):
        liab.append(amount)
    return np.array(liab)




####################################################################### TESTING TESTING TESTING


if __name__ == "__main__":
    # The following two functions create our sql database and insert our bonds into it
    sql_database_setup()
    inserting_bonds()
    # The next function pulls the bond portfolio from the sql database and stores them in an array
    bond_portfolio = bond_portfolio_creation()

    # Here we store our liability amount and duration
    liability_amount = 15000
    liability_length = 20
    # We create an array of outgoing cashflows based on the liability amount and duration
    liability_cashflow = []
    for i in range(liability_length):
        liability_cashflow.append(liability_amount)

    liability_cashflow = np.array(liability_cashflow) # Convert array to numpy array


    esg = StochasticRateESG(0.03) # Create stochastic interest rates based on a flat rate of 0.03
    rate_paths = esg.generate(500, liability_length) # We are generating 500 different scenarios of randomly changing interest rates


    # Array of cash flows from each bond
    # Given a bond's information, bond_cashflows() generates an array that is the cash flow that the bond will generate
    cashflows = [] 
    for bond in bond_portfolio:
        cashflows.append(bond_cashflows(bond.face, bond.coupon, 1, liability_length))
    

    # To create our surplus we create an empty array of 0s that is the same length as our liability payment
    # We then add in all of the cash flows of each bond in our portfolio
    # We then subtract our outgoing liability cash flows to create the surpluses
    surplus = []
    for i in range(len(cashflows[0])):
        surplus.append(0)

    for i in range(len(bond_portfolio)):
        surplus = surplus + cashflows[i]

    surplus = surplus - liability_cashflow

    # Calculating the present value of our liabilities based on our stochastic changing interest rates
    # Doing the same for the assets
    liab_pvs = [present_value_stochastic(liability_cashflow, path) for path in rate_paths]
    asset_pvs_per_path = []
    for path in rate_paths:
        total = 0.0
        for cf in cashflows:
            total += present_value_stochastic(cf, path)
        asset_pvs_per_path.append(total)

    # Calculating surpluses based on assets and liabilities for changing interest rates
    surplus_paths = [
        asset_pvs_per_path[i] - liab_pvs[i]
        for i in range(len(rate_paths))
    ]

    
    print("Liability Present Values: ", liab_pvs)
    print("Asset Present Values: ", asset_pvs_per_path)
    print("Surplus Distribution: ", surplus_paths)

    # Finding out how many scenarios in which our outgoing liability cash flows were greater than our incoming bond portfolio cash flows 
    negatives = sum(1 for s in surplus_paths if s < 0)
    print(f"Number of negative surplus scenarios: {negatives} out of {len(surplus_paths)}")

    # Visualizing all of our data using graph.py (matplotlib.pyplot)
    visualizing_data(surplus_paths)